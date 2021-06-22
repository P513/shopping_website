from django.urls import path
from .views import ProductDetailView, Product_RegisterView, ProductListView


app_name = 'product'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    # path(''), = 등록된 상품들 보기 -> 구매버튼 클릭시 order로
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('register/', Product_RegisterView.as_view(), name='register'),
]
