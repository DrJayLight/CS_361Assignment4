"""CS_361Assignment4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#from django.conf.urls import url
from django.contrib import admin
import views
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^addteacher/$',views.add_teacher),
    url(r'^all-teachers/$',views.all_teachers),
    url(r'^addstudent/$',views.add_student),
    url(r'^all-students/$',views.all_students),
    url(r'^addcourse/$',views.add_course),
    url(r'^all-courses/$',views.all_courses),
    url(r'^enroll-student/$',views.enroll_student),
    #url(r'^all-enrolled-students/$',views.all_enrolled_students)
]


urlpatterns+=staticfiles_urlpatterns()
