from rest_framework import serializers
from .models import Project, Target

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Target
        fields='__all__'