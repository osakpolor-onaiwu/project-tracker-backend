from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import FeedBack


class FeedBackSerializers(serializers.ModelSerializer):
    class Meta:
        model=FeedBack
        fields='__all__'