from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    ProjectTitle=models.CharField(max_length=50,unique=True)
    Start=models.DateField(editable=True)
    End=models.DateField(editable=True)
    Description=models.TextField(max_length=1000)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="projects",null=True)
    created_at=models.DateTimeField(auto_now=True)


    def __str__ (self):
        return self.ProjectTitle


    def was_created_recently (self):
        return self.created_at >=timezone.now()-datetime.timedelta(days=4000)

class Target(models.Model):
    Target=models.TextField(max_length=500)
    Start=models.DateField(editable=True)
    End=models.DateField(editable=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE,null=True,related_name="target")
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Target

    def was_created_recently (self):
        return self.created_at >=timezone.now()-datetime.timedelta(days=4000)
