from django.urls import path
from .views import HomePageView, DetailPageView, ContactPageView, CategoryPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('category/', CategoryPageView.as_view(), name='category'),
    path('<int:pk>', DetailPageView.as_view(), name='post_detial'),
]
