from django.urls import path, include
from Exercise_3.api.views import RoutorListAPIView, RouterCraeteView, RouterRUDAPIView

urlpatterns = [

    path("routor/",
         RoutorListAPIView.as_view(),
         name="router-list"),
    path("routor/<int:pk>/",
         RouterRUDAPIView.as_view(),
         name="router-details"),
    path("routor/create/",
         RouterCraeteView.as_view(),
         name="create-router"),

]