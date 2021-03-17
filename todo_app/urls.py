from django.urls import path,include
from .views import get,delete,update


urlpatterns = [
    path('', get, name="default" ),
    path('delete/<str:id>/',delete, name="delete"),
    path('update/<str:id>/',update, name="update")
]
