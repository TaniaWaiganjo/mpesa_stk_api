# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class AccessToken(models.Model):
	token = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		get_latest_by = 'created_at'

	def __str__(self):
		return self.token
	

from django.db import models

class CallbackData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return f"CallbackData {self.id} at {self.timestamp}"
