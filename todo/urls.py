from django.urls import path
from .views import test,delete



urlpatterns = [
   path('',test,name='todo'),
   path('delete/<int:todo_id>/',delete,name="delete"),
]



