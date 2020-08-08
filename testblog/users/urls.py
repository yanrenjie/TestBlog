# 进行Users子应用的视图路由

from django.urls import path
from users.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register')
]