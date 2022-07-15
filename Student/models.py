from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import uuid 
from datetime import datetime

User = get_user_model()

class Student(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	id_user = models.IntegerField(null=True)
	email = models.EmailField(max_length=255)
	preference = models.CharField(max_length=255,null=True)
	biograpghy = models.TextField(blank=True,null=True)
	def __str__(self):
		return self.user.username

