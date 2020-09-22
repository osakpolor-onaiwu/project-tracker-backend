from rest_framework import routers
from .api import FeedBackViewset

router=routers.DefaultRouter()
router.register('api/projectP/feedbacks', FeedBackViewset, basename='feedback')
urlpatterns=router.urls