from django.conf import settings
from django.db import models


class Fields (models.Model):
	
	data1 = models.CharField(max_length=255)
	data2 = models.CharField(max_length=255)

