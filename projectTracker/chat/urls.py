from rest_framework import routers
from .api import ChatViewset,CommentViewset

router=routers.DefaultRouter()
router.register('api/projectP/chats', ChatViewset, basename='chats')
router.register('api/projectP/comments', ChatViewset, basename='comments')

urlpatterns=router.urls