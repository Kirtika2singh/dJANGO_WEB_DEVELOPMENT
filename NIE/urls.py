"""
URL configuration for NIE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from CSE import views


from CSE.views import Forms, StudentList, StudentDetail, StudentUpdate, StudentDelete

urlpatterns = [
 
path('home', views.home , name = "home"),
path('students', views.students , name = "students"),
    path('forms', Forms.as_view(), name = 'forms'),
    path('', StudentList.as_view(), name = 'list'),
    path('<pk>/detail', StudentDetail.as_view(), name = 'detail'),
    path('<pk>/update', StudentUpdate.as_view(), name = 'update'),
    path('<pk>/delete', StudentDelete.as_view(), name = 'delete'),
    path('index/', views.index , name = "index"),
path('about/', views.about , name = "about"),
path('blog/', views.blog , name = "blog"),
path('contact/', views.contact , name = "contact"),
path('portfolio/', views.portfolio , name = "portfolio"),
]
