from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
