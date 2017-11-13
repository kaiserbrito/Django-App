from django.shortcuts import render
from django.views.generic import View
from . import views
from .forms import UserForm
from .models import User

class Home(View):
    def get(self, request, *args):
        return render(request, 'home.html')


def user_list(request):
    users = User.objects.all()
    return render(request, 'list.html', {'users': users})