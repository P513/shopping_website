from django.http.response import HttpResponseRedirect
from .forms import SignUpForm
from .forms import LoginForm
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
            return redirect('user:login')
        return render(request, self.name, {'form': form})


class LoginView(FormView):
    template_name = 'login.html'

    form_class = LoginForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # user DB 추가하는 구문 넣어야하나
            return render(request, 'index.html')
        return render(request, self.name, {'form': form})
