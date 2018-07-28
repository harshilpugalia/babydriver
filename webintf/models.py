# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Driver(models.Model):
	driver_uid = models.IntegerField(primary_key = True)
	driver_mobnum = models.IntegerField(max_length=12)
	driver_name = models.CharField(max_length=21)
	driver_vehnum = models.IntegerField(max_length=4)
	driver_operator = models.CharField(max_length=100)
	driver_signup_timestamp = models.DateTimeField()

	
