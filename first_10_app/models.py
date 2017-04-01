# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError

from django.db import models


# Create your models here.
class Member(models.Model):
	name = models.CharField(max_length = 120)
	name0 = models.CharField(max_length = 120)
	name1 = models.CharField(max_length = 120)
	name2 = models.CharField(max_length = 120)
	name3 = models.CharField(max_length = 120)
	name4 = models.CharField(max_length = 120)

	def __unicode__(self):
			return self.name