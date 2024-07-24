from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('addRecord', views.addRecord, name='addRecord'),
    path('updateRecord/<int:pk>', views.updateRecord, name='updateRecord'),
    path('view-record/<int:pk>', views.viewRecord, name='view-record'),
    path('delete-record/<int:pk>', views.deleteRecord, name='delete-record'),

]