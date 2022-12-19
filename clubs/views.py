from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Clubs
from .serializers import ClubsSerializer
from .permissions import OwnerOnly
# Create your views here.

class ClubsListCreateView(ListCreateAPIView):
    
    queryset=Clubs.objects.all()
    serializer_class=ClubsSerializer
    
class ClubsDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Clubs.objects.all()
    serializer_class=ClubsSerializer
    permission_classes=[OwnerOnly]