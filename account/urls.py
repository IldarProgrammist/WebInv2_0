from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import Wellcome

urlpatterns = [
    path('', Wellcome.as_view(), name=''),
    path('account/login/',LoginView.as_view(),  name='login'),
    path('account/logout/',LogoutView.as_view(next_page='/'),  name='logout')
]