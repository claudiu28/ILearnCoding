from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import uuid 
from datetime import datetime

User = get_user_model()

class Teacher(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	id_user = models.IntegerField(null=True)
	email = models.EmailField(max_length=255)
	preference = models.CharField(max_length=255,null=True)
	biograpghy = models.TextField(blank=True,null=True)
	def __str__(self):
		return self.user.username


class Courses(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,null=False)
    prof_user = models.CharField(max_length=255,null = True)
    text = models.TextField(max_length=1000,null = True)
    file = models.FileField(upload_to = "files",null = True)
    imag = models.ImageField(upload_to = "imag",null = True)     
    creation_at = models.DateTimeField(default=datetime.now,null = True)

    def __str__(self):
        return self.prof_user

