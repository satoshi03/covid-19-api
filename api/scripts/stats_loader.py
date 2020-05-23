from datetime import datetime
import json
import urllib.request

from django.db.models import Sum

from stats.models import Prefecture, InfectionStats


PREF_STATS_BASE_URL='https://hazard.east.edge.storage-yahoo.jp/covid19/prefectures_graph_{prefecture_id}.json?timestamp={timestamp}t'
MAX_PREF_ID=47

def update_prefectures_stats():
    t = datetime.now()
    for id in range(1, MAX_PREF_ID+1):
        pref = Prefecture.objects.get(id=id)
        print("Fetch stats:{}".format(pref.name))
        url = PREF_STATS_BASE_URL.format(prefecture_id=id, timestamp=t.strftime('%Y%m%d%H%M'))
        with urllib.request.urlopen(url) as response:
           resp = response.read()
           data = json.loads(resp.decode('utf8'))
           for daily_data in data['days']:
               date = datetime.strptime(daily_data['date'], '%Y/%m/%d')
               obj = InfectionStats.objects.filter(reported_date=date, prefecture__id=id)
               if obj:
                   print("Update stats:{} of {}".format(daily_data['date'], pref.name))
                   obj[0].current_infected = daily_data['current']
                   obj[0].new_infected = daily_data['new']
                   obj[0].total_infected = daily_data['total']
                   obj[0].total_recovered = daily_data['recovery']
                   obj[0].total_death = daily_data['death']
                   obj[0].save()
               else:
                   print("Save stats:{} of {}".format(daily_data['date'], pref.name))
                   stats = InfectionStats(
                       prefecture=pref,
                       reported_date=date,
                       restraint_ratio=None,
                       current_infected=daily_data['current'],
                       new_infected=daily_data['new'],
                       total_infected=daily_data['total'],
                       total_recovered=daily_data['recovery'],
                       total_death=daily_data['death'],
                   )
                   stats.save()


JAPAN_STATS_BASE_URL = "https://hazard.east.edge.storage-yahoo.jp/covid19/japan_graph.json?timestamp={timestamp}t"
PREF_ID_OTHER = 48


def update_others_stats():
    t = datetime.now()
    url = JAPAN_STATS_BASE_URL.format(timestamp=t.strftime('%Y%m%d%H%M'))
    with urllib.request.urlopen(url) as response:
        resp = response.read()
        data = json.loads(resp.decode('utf8'))
        pref = Prefecture.objects.get(id=PREF_ID_OTHER)
        for daily_data in data['days']:
            date = datetime.strptime(daily_data['date'], '%Y/%m/%d')
            obj = InfectionStats.objects.filter(reported_date=date).exclude(prefecture__id=PREF_ID_OTHER).aggregate(
                Sum('current_infected'),
                Sum('total_infected'),
                Sum('new_infected'),
                Sum('total_recovered'),
                Sum('total_death'),
            )

            if not obj['current_infected__sum'] or not obj['total_infected__sum'] or not obj['new_infected__sum'] \
                    or not obj['total_recovered__sum'] or not obj['total_death__sum']:
                continue

            #
            # その他の感染者数 = 日本全国の感染者数 - 各都道府県の感染者数の合計
            #
            current = daily_data['current'] - obj['current_infected__sum']
            new = daily_data['new'] - obj['new_infected__sum']
            total = daily_data['total'] - obj['total_infected__sum']
            recovered = daily_data['recovery'] - obj['total_recovered__sum']
            death  = daily_data['death'] - obj['total_death__sum']

            print(current, new, total, recovered, death)
            obj = InfectionStats.objects.filter(reported_date=date, prefecture__id=PREF_ID_OTHER)
            if obj:
                print("Update stats:{} of {}".format(daily_data['date'], pref.name))
                obj[0].current_infected = current
                obj[0].new_infected = new
                obj[0].total_infected = total
                obj[0].total_recovered = recovered
                obj[0].total_death = death
                obj[0].save()
            else:
                print("Save stats:{} of {}".format(daily_data['date'], pref.name))
                stats = InfectionStats(
                    prefecture=pref,
                    reported_date=date,
                    restraint_ratio=None,
                    current_infected=current,
                    new_infected=new,
                    total_infected=total,
                    total_recovered=recovered,
                    total_death=death,
                )
                stats.save()


def run():
    update_prefectures_stats()
    update_others_stats()
