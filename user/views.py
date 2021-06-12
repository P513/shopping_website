from django.http.response import HttpResponseRedirect
from user.forms import SignUpForm
from .models import User
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView


def index(request):
    return render(request, 'index.html')


class SignUpView(FormView):
    template_name = 'signup.html'

    form_class = SignUpForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # user DB 추가하는 구문 넣어야하나
            return HttpResponseRedirect('login.html')
        return render(request, self.name, {'form': form})
