from django.urls import path
from .import views
urlpatterns = [
    path('get-document/<int:id>/', views.Get_Document, name='get_document'),
]