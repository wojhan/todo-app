from django.urls import path

from . import views

urls = [
    path("cases/", views.CaseList.as_view()),
    path("cases/<int:pk>/", views.CaseDetail.as_view()),
    path("cases/<int:case_pk>/tasks/", views.CaseTaskList.as_view()),
    path("tasks/<int:pk>", views.TaskDetail.as_view()),
]
