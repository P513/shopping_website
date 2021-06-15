from .forms import SignUpForm
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView


def index(request):
    return render(request, 'index.html', {'user': request.session.get('user')})


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
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
            self.request.session['user'] = form.data.get('grade')
            # return render(request, 'product:products')
            return render(request, 'index.html')
        return render(request, self.template_name, {'form': form})
