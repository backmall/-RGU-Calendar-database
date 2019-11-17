from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from events.models import Event
from .forms import UserUpdateForm, UserRegisterForm, ProfileUpdateForm
# from django.views.generic import DetailView



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

#personalising site with Profile access
@login_required
def profile(request):
	# UPDATING USER PROFILE BELOW - validation, POST and FIELD request
	if request.method == 'POST':
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			# some user feedback same as in UserRegistaraion
			messages.success(request, f'Account updated!')
			return redirect('profile')
	else:
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'events': Event.objects.filter(author=request.user),
		'user_form': user_form,
		'profile_form': profile_form,
	}
	return render(request, 'users/profile.html', context)


# class ProfileDetailView(DetailView):
# 	model = User
# 	template_name = 'user_detail.html'

# 	def get_user_profile(self, username):   
# 		return get_object_or_404(User, pk=username)

# 	def profile_detail(self, **kwargs):
# 		context = super(ProfileDetailView, self).get_context_data(**kwargs)
# 		return context  