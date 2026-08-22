from django.urls import path
from . import views


urlpatterns = [
    path('communities/', views.communities, name='communities'),

]