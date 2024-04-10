from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('update/<int:pk>/', views.update_user, name='update'),
    path('delete/<int:pk>/', views.delete_user, name='delete'),
]