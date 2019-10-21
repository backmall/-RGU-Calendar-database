from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.db import models


from .models import Event
from django.contrib.auth.models import User



def index(request):
	context = {
		'events': Event.objects.all()	
	}
	return render(request, 'events/index.html', context)

class EventListView(ListView):
	model = Event
	template_name = 'events/base.html' # <app> /<model>_<viewtype>.html
	context_object_name = 'event'
	ordering = ['-datetime_event']


class EventDetailView(DetailView):
	model = Event

	def event_detail(request, pk):
		context = {
			'events': Event.objects.filter(pk=pk)
		}
		return render(request, 'event_detail.html', context)

class EventCreateView(LoginRequiredMixin, CreateView):
	model = Event

	fields = [
		'event_name', 
		'datetime_event',
		'description',
		'location',
		'author'
	]
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
