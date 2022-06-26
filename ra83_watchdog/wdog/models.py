from django.db import models


class Worker(models.Model):
    has_token = models.BooleanField(default=False)
    token = models.CharField(max_length=100, blank=True)
    req = models.CharField(max_length=100, blank=True)
    in_sc = models.BooleanField(default=False)
