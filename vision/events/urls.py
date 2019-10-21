from django.urls import path
from . import views
from events.views import EventListView, EventCreateView, EventDetailView

urlpatterns = [
    path('', views.index, name='home-events'),
    path('events/new/', EventCreateView.as_view(), name='event-form'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),

]