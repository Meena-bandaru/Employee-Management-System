from django.db import models


class Organization(models.Model):
    org_id = models.IntegerField()
    name = models.CharField(max_length=100, default="")
