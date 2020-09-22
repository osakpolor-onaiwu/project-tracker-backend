from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.
class FeedBack(models.Model):
    FirstName=models.CharField(max_length=25)
    LastName=models.CharField(max_length=25)
    Email=models.EmailField()
    Comment=models.TextField()
    created_at=models.DateTimeField(auto_now=True)


    def __str__ (self):
        return self.FirstName


    def was_created_recently (self):
        return self.created_at >=timezone.now()-datetime.timedelta(days=4000)