from rest_framework import viewsets
from ..serializers.ProjectSerializer import ProjectSerializer
from ..project import Project
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

class ProjectDetailView(APIView):
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        project = Project.objects.filter(id=kwargs['pk'])
        serializer = ProjectSerializer(project, context={"request": request}, many=True)
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)

class ProjectListView(APIView):
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        project = Project.objects.filter(product=kwargs['pk'])
        serializer = ProjectSerializer(project, context={"request": request}, many=True)
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)

