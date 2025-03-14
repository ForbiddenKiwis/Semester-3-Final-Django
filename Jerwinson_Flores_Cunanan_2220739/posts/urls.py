from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('details/<int:post_id>', views.details, name='post_details'),

]