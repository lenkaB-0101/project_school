from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('teachers', views.TeacherViewset)
router.register('subjects', views.SubjectViewset)

urlpatterns = [
#    path("hello_world", views.hello_world, name="hello_world"),
#    path('subjects', views.list_subjects, name="list_subjects"),
#    path('subjects/<int:pk>', views.subject_detail, name="subject_detail"),
    path('', include(router.urls))
]

