from order.forms import OrderForm
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import OrderForm


class OrderView(FormView):
    form_class = OrderForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/product/detail/'+str(form.product))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw
