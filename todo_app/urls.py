from django.urls import path,include
from .views import get,delete,update,loginPage,register, logoutPage


urlpatterns = [
    path('', get, name="default" ),
    path('delete/<str:id>/',delete, name="delete"),
    path('update/<str:id>/',update, name="update"),
    path('login',loginPage,name="login"),
    path('register',register,name="register"),
    path('logout',logoutPage,name="logout")

]
