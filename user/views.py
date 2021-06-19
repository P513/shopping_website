from django.views.generic.list import ListView
from .forms import SignUpForm
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .models import User


def index(request):
    return render(request, 'index.html', {'user': request.session.get('userid')})


def logout(request):
    if request.session.get('userid'):
        del(request.session['userid'])
    return redirect('user:login')


class SignUpView(FormView):
    template_name = 'signup.html'

    form_class = SignUpForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return redirect('user:login')
        else:
            return render(request, self.template_name, {'form': form})


class LoginView(FormView):
    template_name = 'login.html'

    form_class = LoginForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.request.session['userid'] = form.data.get('userid')
            # return render(request, 'product:products')
            return render(request, 'index.html', {'user': request.session.get('userid')})
        return render(request, self.template_name, {'form': form})


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
