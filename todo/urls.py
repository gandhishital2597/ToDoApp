from django.urls import path

from .views import *
urlpatterns=[
    path('addTask/',addTask,name='addTask'),
    path('mark_as_done/<int:pk>/',mark_as_done,name='mark_as_done'),
    path('mark_as_undone/<int:pk>/', mark_as_undone, name='mark_as_undone'),

    #EDIT/Update Feature
    path('edit_task/<int:pk>/',edit_task,name='edit_task'),
    #DELETE Feature
    path('delete_task/<int:pk>/',delete_task,name='delete_task'),
]