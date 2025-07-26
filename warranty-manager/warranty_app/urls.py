from .import views
from django.urls import path

urlpatterns = [
    path('',views.Home,name='Home'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.login_view,name='logout'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('file-upload/',views.file_upload,name='file_upload'),
    path('warranty-form/', views.Warranty_form, name='warranty_form'),

]
