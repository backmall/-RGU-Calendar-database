from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView
from django.db import models
from django.contrib.auth.models import User
from .models import Event




def index(request):
	context = {
		'events': Event.objects.all()	
	}
	return render(request, 'events/index.html', context)

class EventListView(ListView):
	model = Event
	template_name = 'events/base.html' # <app> /<model>_<viewtype>.html
	context_object_name = 'event'
	# queryset = Event.objects.order_by('start_date')
	ordering = ['-date_published']


class EventDetailView(DetailView):
	model = Event

	def event_detail(request, pk):
		context = {
			'events': Event.objects.filter(pk=pk)
		}
		return render(request, 'event-detail.html', context)


class EventCreateView(LoginRequiredMixin, CreateView):
	model = Event

	fields = [
		'event_name', 
		'start_date',
		'start_time',
		'end_date',
		'end_time',
		'description',
		'location',
		'image',
	]

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

def staff(request):
	context = {
		'users': User.objects.all()
	}
	return render(request, 'users/staff.html',  context)
