from django.shortcuts import render
from django.views.generic import View

class Home(View):
    def get(self, request, *args):
        return render(request, 'home.html')
