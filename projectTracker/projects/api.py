from projects.models import Project, Target
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer, TargetSerializer

#viewsets
class ProjectVeiwset(viewsets.ModelViewSet):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    serializer_class=ProjectSerializer
    def get_queryset(self):
        return self.request.user.projects.all().order_by('created_at')
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class TargetVeiwset(viewsets.ModelViewSet):
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=TargetSerializer

    def get_queryset(self):
        return self.request.Project.target.all().order_by('created_at')
