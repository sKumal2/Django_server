from django.urls import path
from . import views


urlpatterns = [
    path('communities/', views.communities, name='communities'),
    path('communities/<slug:slug>/', views.community_detail, name='community_detail'),

]