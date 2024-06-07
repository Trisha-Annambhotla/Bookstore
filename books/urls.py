from django.urls import path
from . import views

urlpatterns = [
    path('',views.books,name='books'),
    path('details/<int:id>',views.details,name='details')
    ]