from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(active=True)
    serializer_class = ItemSerializer
