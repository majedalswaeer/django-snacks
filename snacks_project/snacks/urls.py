from django.urls import path
from .views import HomeView,AboutUsView,BaseView
urlpatterns=[
    path('',BaseView.as_view(),name='base'),
    path('home',HomeView.as_view(),name='home'),
    path('aboutus',AboutUsView.as_view(),name='aboutus')
]