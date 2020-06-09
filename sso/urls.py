from django.contrib import admin
from django.urls import path
from django.conf import settings

from useraccounts.factories import User_view_factory
from .views import ViewWrapper

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', ViewWrapper.as_view(view_factory = User_view_factory), name= 'user_view_factory'),
    path('user/id/<int:init_id>/', ViewWrapper.as_view(view_factory = User_view_factory), name='User_view_factory'),
   
]