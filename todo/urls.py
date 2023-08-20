from django.urls import path
from . import views 


urlpatterns = [
    path('addTask/', views.addTask, name="addTask"),
    # mark_as_undone feature
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    # Mark as done feature
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    # Edit fearure.
    path('edit_tasks/<int:pk>/', views.edit_task, name='edit_tasks'),
    # delete task 
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]