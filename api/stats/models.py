from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class Prefecture(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = _('都道府県')

    code = models.PositiveSmallIntegerField(_('都道府県コード'))
    name = models.CharField(_('都道府県名'), max_length=10)
    name_en = models.CharField(_('都道府県名(英語)'), max_length=20)

    def __str__(self):
        return self.name


class InfectionStats(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = _('感染統計')
        unique_together = (('prefecture', 'reported_date'))

    prefecture = models.ForeignKey(Prefecture, on_delete=models.PROTECT)
    new_infected = models.IntegerField(_('新規感染者数'), default=0)
    current_infected = models.IntegerField(_('現在感染者数'), default=0)
    total_infected = models.IntegerField(_('累計感染者数'), default=0)
    total_recovered = models.IntegerField(_('回復者数'), default=0)
    total_death = models.IntegerField(_('死者数'), default=0)
    restraint_ratio = models.FloatField(_('自粛率'),
                                        null=True,
                                        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    reported_date = models.DateField(_('報告日付'), db_index=True)
    created_at = models.DateTimeField(_('作成日時'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新日時'), auto_now=True)

    @classmethod
    def aggregate_by_date(cls, date):
        return cls.objects.filter(reported_date=date).aggregate(Sum('patients'), Sum('deaths'))

    def __str__(self):
        return "{}:{}".format(self.reported_date, self.prefecture.name)


class BehaviorStats(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = _('行動統計')
        unique_together = (('prefecture', 'reported_date'))

    prefecture = models.ForeignKey(Prefecture, on_delete=models.PROTECT)
    restraint_ratio = models.FloatField(_('自粛率'),
                                        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    reported_date = models.DateField(_('報告日付'), db_index=True)

    @classmethod
    def aggregate_by_date(cls, date):
        return cls.objects.filter(reported_date=date).aggregate(Sum('reported_date'))

    def __str__(self):
        return "{}:{}".format(self.reported_date, self.prefecture.name)
