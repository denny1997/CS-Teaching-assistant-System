"""CS_teaching_record_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import *

from . import controller

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^add-course$', controller.add_course),
    url(r'^list-course$', controller.list_course),
    url(r'^modify-course$', controller.modify_course),
    url(r'^delete-course$', controller.delete_course),
    url(r'^add-faculty$', controller.add_faculty),
    url(r'^list-faculty$', controller.list_faculty),
    url(r'^modify-faculty$', controller.modify_faculty),
    url(r'^delete-faculty$', controller.delete_faculty),
    url(r'^add-teaches$', controller.add_teaches),
    url(r'^list-teaches$', controller.list_teaches),
    url(r'^delete-teaches$', controller.delete_teaches),
    url(r'^list-free-faculty$', controller.list_free_faculty),
    url(r'^get-enroll-data$', controller.get_enroll_data),
    url(r'^import-course-data$', controller.import_course_data),
    url(r'^import-faculty-data$', controller.import_faculty_data),
    url(r'^import-teaches-data$', controller.import_teaches_data),
    url(r'^get-keywords-scores$', controller.get_keywords_scores),
    url(r'^get-area-data$', controller.get_area_data),
    url(r'^get-enroll-data-faculty$', controller.get_enroll_data_faculty),
    url(r'^get-recommendation$', controller.get_recommendation),
]
