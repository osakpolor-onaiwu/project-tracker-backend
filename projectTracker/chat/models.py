from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    message=models.TextField()
    image=models.ImageField(upload_to ='uploads/% Y/% m/% d/',width_field="200px",height_field="300px",null=True,blank=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="chats",null=True)
    created_at=models.DateTimeField(auto_now=True)


    def __str__ (self):
        return self.message


    def was_created_recently (self):
        return self.created_at >=timezone.now()-datetime.timedelta(days=4000)

class Comment(models.Model):
    message=models.TextField()
    comment=models.ForeignKey(Chat,on_delete=models.SET_NULL,related_name="comments",null=True)
    image=models.ImageField(upload_to ='uploads/% Y/% m/% d/',width_field="200px",height_field="300px",null=True,blank=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments",null=True)
    created_at=models.DateTimeField(auto_now=True)


    def __str__ (self):
        return self.message


    def was_created_recently (self):
        return self.created_at >=timezone.now()-datetime.timedelta(days=4000)