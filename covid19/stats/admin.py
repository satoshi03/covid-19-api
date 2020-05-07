from django.contrib import admin

from .models import Prefecture, InfectionStats, BehaviorStats


@admin.register(Prefecture)
class PrefectureAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'name_en')


@admin.register(InfectionStats)
class InfectionStatsAdmin(admin.ModelAdmin):
    list_display = ('prefecture', 'patients', 'deaths', 'reported_date')


@admin.register(BehaviorStats)
class BehaviorStatsAdmin(admin.ModelAdmin):
    list_display = ('prefecture', 'restraint_ratio', 'reported_date')
