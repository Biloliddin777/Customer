from django.contrib import admin
from django.urls import path

from my_project.views import views, auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project-management/', views.project_management, name='project_management'),
    path('customers/', views.customers, name='customers'),
    path('customer-details/<int:customer_id>/', views.customer_details, name='customer_details'),
    path('user/profile/', views.profile, name='profile'),
    path('settings/', views.profile_settings, name='profile_settings'),
    path('add-customer/', views.add_customer, name='add_customer'),
    path('edit-customer/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('delete-customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),


    path('logout/', auth.logout_page, name='logout_page'),
    path('authentication/login/', auth.login_page, name='login_page'),
    path('authentication/register/', auth.register_page, name='register_page'),
]
