from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name="home"),
    path('task/',views.task,name="task"),
    path('edit/<title>/',views.edit,name='edit'),
    path('delete/<title>/',views.delete,name='delete')
]
