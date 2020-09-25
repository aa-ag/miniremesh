from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addconversation/', views.addConversation, name='addconversation'),
    path('convodetail/<int:id>', views.convoDetail, name='convodetail'),
    path('addmessage/<int:id>', views.addMessage, name='addmessage'),
    path('search/', views.search, name='search'),
]