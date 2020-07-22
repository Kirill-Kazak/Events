from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)
from bookshop.serializer import EventSerializer

from bookshop.models import Event


class ListEvent(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class CreateEvent(CreateAPIView):
    serializer_class = EventSerializer

class RetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
