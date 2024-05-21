from django.urls import path
from . import views
from .views import donation_record,  records_list, delete_donation, update_donation
urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'), 
    path('register/', views.register_user, name='register'), 
    path('record/<int:pk>/', donation_record, name='record'), 
    path('records/', records_list, name='records_list'),
    path('delete_donation/<int:pk>/', delete_donation, name='delete_donation'),
    path('add_donation/', views.add_donation, name='add_donation'), 
    path('update_donation/<int:pk>/', views.update_donation, name='update_donation'),




]

