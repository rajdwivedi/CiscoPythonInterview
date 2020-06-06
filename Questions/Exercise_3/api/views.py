from rest_framework import viewsets, generics,  status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from Exercise_3.api.serializers import RouterSerializer
from Excercise_1.models import RoutorDetail

from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(request)


class RoutorListAPIView(generics.ListAPIView):
    queryset = RoutorDetail.objects.all()
    serializer_class = RouterSerializer
    permission_classes = [IsAuthenticated]


class RouterCraeteView(generics.CreateAPIView):
    queryset = RoutorDetail.objects.all()
    serializer_class = RouterSerializer
    permission_classes = [IsAuthenticated, IsAdminUser ]

    def perform_create(self, serializer):
        serializer.save()


class RouterRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoutorDetail.objects.all()
    serializer_class = RouterSerializer
    permission_classes = [IsAuthenticated]
