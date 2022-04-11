from django.conf import settings
from django.db import models


class CycleData(models.Model):
    "Generated Model"
    cycleLength = models.BigIntegerField()
    lastStartDay = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )
    periodLength = models.BigIntegerField(
        null=True,
        blank=True,
    )
