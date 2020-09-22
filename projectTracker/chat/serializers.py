from rest_framework import serializers
from .models import Chat,Comment

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chat
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'