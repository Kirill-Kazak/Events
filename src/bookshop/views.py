from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)
from bookshop.serializer import EventSerializer
from bookshop.models import Event
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q


class ListEvent(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class CreateEvent(CreateAPIView):
    serializer_class = EventSerializer

class RetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    
class GetEvents(APIView):
    def get(self, request, date):
        date = date.split('-')
        if len(date) == 1:
            response = Event.objects.filter(
                Q(date_stop__year=date[0])
            )
        elif len(date) == 2:
            response = Event.objects.filter(
                Q(date_stop__year=date[0]) &
                Q(date_stop__month=date[1])
            )
        elif len(date) == 3:
            response = Event.objects.filter(
                Q(date_stop__year=date[0]) &
                Q(date_stop__month=date[1]) &
                Q(date_stop__day=date[2])
            )
        serializer = EventSerializer(response, many=True)
        return Response(serializer.data)
