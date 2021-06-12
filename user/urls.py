from django.urls import path
from .views import SignUpView


from . import views


app_name = 'user'

urlpatterns = [
    #    path('questions', views.index, name='index'),
    path('', views.index, name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
