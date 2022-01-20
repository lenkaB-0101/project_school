from django.urls import path

from . import views

urlpatterns = [
    path('subjects', views.list_subjects, name="list-subjects"),
    path('subjects/<int:pk>', views.subject_detail, name="subject_detail")
]
