"""eportfolioforpreschoolstudent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('referanslar/', views.referanslar, name='referanslar'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('home/', include('home.urls')),
    path('student/', include('student.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('students/', views.list_students, name ='list_students'),
    path('mystudent/<int:id>/<slug:slug>/', views.student_detail, name ='student_detail'),
    path('materyal/<int:st_id>/<int:m_id>/<slug:slug>/', views.material_detail, name='material_detail'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)