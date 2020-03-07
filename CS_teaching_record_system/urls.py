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
    url(r'^index$', controller.index),
    url(r'^add-course$', controller.add_course),
    url(r'^add-course-form$', controller.add_course_form),
    url(r'^list-course$', controller.list_course),
    url(r'^modify-course$', controller.modify_course),
    url(r'^modify-course-form$', controller.modify_course_form),
    url(r'^delete-course$', controller.delete_course),
    url(r'^add-faculty$', controller.add_falculty),
    url(r'^add-faculty-form$', controller.add_faculty_form),
    url(r'^list-faculty$', controller.list_faculty),
    url(r'^modify-faculty$', controller.modify_faculty),
    url(r'^modify-faculty-form$', controller.modify_faculty_form),
    url(r'^delete-faculty$', controller.delete_faculty),
]
