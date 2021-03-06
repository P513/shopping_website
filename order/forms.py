import user
from django import forms
from .models import Order
from product.models import Product
from user.models import User
from django.db import transaction


class OrderForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요.'
        }, label='수량'
    )
    product = forms.IntegerField(
        error_messages={
            'required': '재고를 입력해주세요.'
        }, label='재고', widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        userid = self.request.session.get('userid')

        if quantity and product and userid:
            with transaction.atomic():
                prod = Product.objects.get(pk=product)
                order = Order(
                    quantity=quantity,
                    product=Product.objects.get(pk=product),
                    user=User.objects.get(userid=userid)
                )
                order.save()
                prod.stock -= quantity
                prod.save()

        else:
            self.product = product
            self.add_error('quantity', '수량이 없습니다.')
            self.add_error('product', '상품이 없습니다.')
