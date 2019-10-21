from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from events.models import Event
from .models import User


# Create your views here.

class AuthRequiredMiddleware(object):
	def process_request(self, request):
		if not request.user.is_authenticated():
			return HttpResponseRedirect(reverse('users/register.html')) # or http response
		return None

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created! You can Log In now!')
			return redirect('login')
	else:
		form = UserRegisterForm()
		messages.error(request, f'Something went wrong, try again!')
	# passing in form as context - ditionary of {variable form: newely created form UserCreationForm()}
	return render(request, 'users/register.html', {'form': form})
