from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(),name='category-list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(),name='category-detail'),

    path('product/', ProductListAPIView.as_view(),name='product-list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(),name='product-detail'),

    path('job/', JobListAPIView.as_view(),name='job-list'),
    path('job/<int:pk>/', JobDetailAPIView.as_view(),name='job-detail'),

    path('social_media/', Social_mediaListAPIView.as_view(),name='social_media-list'),
    # path('social_media/<int:pk>/', Social_mediaDetailAPIView.as_view(),name='social_media-detail'),
    
    path('vacancy/', VacancyListAPIView.as_view(),name='vacancy-list'),
    path('vacancy/<int:pk>/', VacancyDetailAPIView.as_view(),name='vacancy-detail'),

    path('aplication/', AplicationListAPIView.as_view(),name='aplication-list'),
    path('aplication/<int:pk>/', AplicationDetailAPIView.as_view(),name='aplication-detail'),

]