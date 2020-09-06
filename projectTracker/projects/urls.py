from rest_framework import routers
from .api import ProjectVeiwset, TargetVeiwset

router=routers.DefaultRouter()
router.register('api/projectP/projects', ProjectVeiwset, basename='projects')
router.register('api/projectP/target', TargetVeiwset, basename='target')

urlpatterns=router.urls