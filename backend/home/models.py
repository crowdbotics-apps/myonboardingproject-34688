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
    cycleData = models.OneToOneField(
        "home.CycleData",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="cycledata_cycleData",
    )
