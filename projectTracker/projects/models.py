from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    ProjectTitle=models.CharField(max_length=50,unique=True)
    User=models.ForeignKey(User,on_delete=models.CASCADE,related_name="project",null=True)
    Start=models.DateField(editable=True)
    End=models.DateField(editable=True)
    Description=models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now=True)

    def was_created_recently (self):
        return self.created_at >=timezone.now()-datetime.timedelta(days=4000)

    def __str__ (self):
        return self.ProjectTitle

class Target(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,null=True,related_name="target")
    Target=models.TextField(max_length=500)
    Start=models.DateField(editable=True)
    End=models.DateField(editable=True)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Target

    def was_created_recently (self):
        return self.created_at >=timezone.now()-datetime.timedelta(days=4000)

    