from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm      # extends from forms.py

class Index(TemplateView):
    template_name = 'inventory/index.html'

class SignUpView(View):
    # request a signup form
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'inventory/signup.html', {'form': form})
    
    # post completed signup form
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():     # if form is valid, save and authenticate
            form.save()
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            login(request, user)
            return redirect('index')
        
        # return user back to signup page in case there is an error
        return render(request, 'inventory/signup.html', {'form': form})