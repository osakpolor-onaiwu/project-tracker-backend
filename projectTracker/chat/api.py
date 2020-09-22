from chat.models import Chat, Comment
from rest_framework import viewsets, permissions
from .serializers import ChatSerializer, CommentSerializer

#viewsets
class ChatViewset(viewsets.ModelViewSet):
    permission_classes=[
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class=ChatSerializer
    def get_queryset(self):
        return self.request.user.chats.all().order_by('created_at')
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class CommentViewset(viewsets.ModelViewSet):
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=CommentSerializer

    def get_queryset(self):
        return self.request.Chat.comments.all().order_by('created_at')
