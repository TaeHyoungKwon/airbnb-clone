from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        abstract = True
