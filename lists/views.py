from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
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
    data = dict()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = UserForm()
    
    context = {'form': form}
    data['html_form'] = render_to_string('add_user.html', context, request=request)
    return JsonResponse(data)