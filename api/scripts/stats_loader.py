from datetime import datetime
import json
import urllib.request


from stats.models import Prefecture, InfectionStats


BASE_URL='https://hazard.east.edge.storage-yahoo.jp/covid19/prefectures_graph_{prefecture_id}.json?timestamp={timestamp}t'
MAX_PREF_ID=47

def run():
    t = datetime.now()
    for id in range(1, MAX_PREF_ID+1):
        pref = Prefecture.objects.get(id=id)
        print("Fetch stats:{}".format(pref.name))
        url = BASE_URL.format(prefecture_id=id, timestamp=t.strftime('%Y%m%d%H%M'))
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
