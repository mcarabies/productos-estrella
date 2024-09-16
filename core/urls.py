from django.urls import path
from .views import home, review, category

urlpatterns = [
    path('', home, name='home'),
    path('category/', category, name='category'),
    path('review/', review, name='review'),
]