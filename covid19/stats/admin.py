from django.contrib import admin

from .models import Prefecture, DailyStats


@admin.register(Prefecture)
class PrefectureAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'name_en')

@admin.register(DailyStats)
class DailyStatsAdmin(admin.ModelAdmin):
    list_display = ('prefecture', 'patients', 'deaths', 'reported_date')
