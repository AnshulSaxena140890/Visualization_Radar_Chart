# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BlackCofferData(models.Model):
	topic = models.CharField(max_length=200)
	sector = models.CharField(max_length=200)
	region = models.CharField(max_length=200)
	pestle = models.CharField(max_length=200)
	year = models.PositiveIntegerField()
	intensity = models.PositiveIntegerField()
	likelihood = models.PositiveIntegerField()
	relevance = models.PositiveIntegerField()










#import json & model------------------

# >>> with open("/home/anshul/projectblk/jsondata.json", "r") as read_file:
# ...     data = json.load(read_file)
# ...     
# ...     for items in data:
# ...       p = BlackCofferData(topic=items['topic'],sector=items['sector'],region=items['region'],pestle=items['pestle'],intensity=items['intensity'],likelihood=items['likelihood'],relevance=items['relevance'],year=(items['added'].split(" "))[2])
# ...       p.save()

