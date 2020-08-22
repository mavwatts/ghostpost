"""django_ghost_post URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from graveyard import views

urlpatterns = [
    path('', views.index_view, name='homepage'),
    path('sortbyvotes/', views.sorted_votes, name='sortbyvotes'),
    path('boasts/', views.boast_view, name='boasts'),
    path('roasts/', views.roast_view, name='roasts'),
    path('generic_form/', views.create_post_view, name='createpost'),
    path('upvote/<int:upvote_id>/', views.upvote_view, name='upvote'),
    path('downvote/<int:downvote_id>/', views.downvote_view, name='downvote'),
    path('admin/', admin.site.urls)
]

