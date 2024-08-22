from django.urls import re_path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    re_path(r'^tasks/$', TaskListView.as_view(), name='task_list'),
    re_path(r'^tasks/add/$', TaskCreateView.as_view(), name='task_add'),
    re_path(r'^tasks/(?P<pk>\d+)/$', TaskDetailView.as_view(), name='task_detail'),
    re_path(r'^tasks/(?P<pk>\d+)/edit/$', TaskUpdateView.as_view(), name='task_edit'),
    re_path(r'^tasks/(?P<pk>\d+)/delete/$', TaskDeleteView.as_view(), name='task_delete'),
]