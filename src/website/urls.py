"""website URL Configuration

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

from blog.views import blog_posts, blog_post, article_post, BlogIndexView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView
from website.views import signup, HomeView

urlpatterns = [
    path('', HomeView.as_view(title = "accueil"), name="home"), #le nom (name) de l'url est "home" et renvoie à la view "home"
    path('about/', HomeView.as_view(title = "à propos"), name="about"),
    path('customadmin/', admin.site.urls),
    path('blog/', BlogIndexView.as_view(), name="blog-index"),
    path('blog/<str:slug>/', BlogPostDetailView.as_view(), name="blog-post"),
    path('blog/<str:slug>/edit/', BlogPostUpdateView.as_view(), name="blog-post-edit"),
    path('blog/<str:slug>/delete/', BlogPostDeleteView.as_view(), name="blog-post-delete"),
    path('signup/', signup, name="signup"),
    path('create-article/', BlogPostCreateView.as_view(), name="article_post")
]