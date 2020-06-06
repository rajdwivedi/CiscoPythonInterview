from rest_framework import viewsets, generics,  status
from rest_framework.permissions import IsAuthenticated

from Exercise_3.api.serializers import RouterSerializer
from Excercise_1.models import RoutorDetail


class RoutorListAPIView(generics.ListAPIView):
    queryset = RoutorDetail.objects.all()
    serializer_class = RouterSerializer
    permission_classes = [IsAuthenticated]


class RouterCraeteView(generics.CreateAPIView):
    queryset = RoutorDetail.objects.all()
    serializer_class = RouterSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class RouterRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoutorDetail.objects.all()
    serializer_class = RouterSerializer
    permission_classes = [IsAuthenticated]
