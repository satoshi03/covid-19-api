from django.db import models
from django.utils.translation import ugettext_lazy as _


class Prefecture(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = _('都道府県')

    code = models.PositiveSmallIntegerField(_('都道府県コード'))
    name = models.CharField(_('都道府県名'), max_length=10)
    name_en = models.CharField(_('都道府県名(英語)'), max_length=20)

    def __str__(self):
        return self.name


class DailyStats(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = _('日別統計')
        unique_together = (('prefecture', 'reported_date'))

    prefecture = models.ForeignKey(Prefecture, on_delete=models.PROTECT)
    patients = models.PositiveIntegerField(_('感染者数'), default=0)
    deaths = models.PositiveIntegerField(_('死者数'), default=0)
    reported_date = models.DateField(_('日付'), db_index=True)

    @classmethod
    def aggregate_by_date(cls, date):
        return cls.objects.filter(date=date).aggregate(Sum('patients'), Sum('deaths'))
