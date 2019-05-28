from django.urls import path, include
from articles import views

urlpatterns = [
    path('articles/', views.archive, name='archive'),
    path('', views.archive, name='archive'),
    path('article/new/', views.create_post, name='create_post'),
    path('article/<article_id>/', views.get_article, name='get_article'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]