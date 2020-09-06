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
        return self.request.user.Project.objects.all().order_by('created_at')
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class TargetVeiwset(viewsets.ModelViewSet):
    queryset=Target.objects.all().order_by('-created_at')
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=TargetSerializer
