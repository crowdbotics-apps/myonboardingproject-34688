from django.conf import settings
from django.db import models


class CycleData(models.Model):
    "Generated Model"
    cycleLength = models.BigIntegerField()
    lastStartDay = models.DateTimeField(
        null=True,
        blank=True,
        auto_now=True,
    )
    periodLength = models.BigIntegerField(
        null=True,
        blank=True,
    )
