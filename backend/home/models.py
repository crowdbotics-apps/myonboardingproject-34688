from django.conf import settings
from django.db import models


class CycleData(models.Model):
    "Generated Model"
    cycleLength = models.BigIntegerField()
