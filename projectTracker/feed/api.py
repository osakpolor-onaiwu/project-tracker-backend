from feed.models import FeedBack
from rest_framework import viewsets, permissions
from .serializers import FeedBackSerializers

class FeedBackViewset(viewsets.ModelViewSet):
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=FeedBackSerializers
    queryset=FeedBack.objects.order_by('created_at')