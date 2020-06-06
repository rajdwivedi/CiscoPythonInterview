from django.urls import path, include
from Exercise_3.api.views import RoutorListAPIView, RouterCraeteView, RouterRUDAPIView, index

urlpatterns = [

    path('', index, name="Routor-index-page"),

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