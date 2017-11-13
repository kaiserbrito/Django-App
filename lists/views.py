from django.shortcuts import render, redirect
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

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})