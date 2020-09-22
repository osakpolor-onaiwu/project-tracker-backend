from rest_framework import routers
from .api import ProjectViewset, TargetViewset, TargetViewsetGet

router=routers.DefaultRouter()
router.register('api/projectP/projects', ProjectViewset, basename='projects')
router.register('api/projectP/target', TargetViewset, basename='target')
router.register('api/projectP/Gettarget', TargetViewsetGet, basename='Gettarget')
urlpatterns=router.urls