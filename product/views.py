from django.shortcuts import render, redirect
from .models import Product
from .forms import RegisterForm
from django.views.generic.edit import FormView


def index(request):
    return render(request, 'index.html')


class Product_RegisterView(FormView):
    template_name = 'product_register.html'

    form_class = RegisterForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return redirect('product:register')
        else:
            return render(request, self.template_name, {'form': form})
