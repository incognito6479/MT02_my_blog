from django.shortcuts import render
from django.views.generic import TemplateView, View 


class HomeView(TemplateView):
    template_name = 'index.html'


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')