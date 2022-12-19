from django.urls import path
from .views import ClubsListCreateView,ClubsDetailView
# Create your urls here.
urlpatterns = [
    path('',ClubsListCreateView.as_view(),name='clubs_list'),
    path('<int:pk>',ClubsDetailView.as_view(),name='clubs_detail'),
]