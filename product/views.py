from order.forms import OrderForm
from .models import Product
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView


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


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    template_name = "product_detail.html"
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context
