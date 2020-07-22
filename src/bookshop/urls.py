from django.urls import path
from bookshop import views

urlpatterns = [
    path('listEvent/', views.ListEvent.as_view()),
    path('createEvent/', views.CreateEvent.as_view()),
    path('RUDEvent/<int:pk>/', views.RetriveUpdateDestroy.as_view()),
    path('get/<str:date>/', views.GetEvents.as_view()),
]