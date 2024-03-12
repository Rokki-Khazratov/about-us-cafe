from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response    
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .models import Category, Product,Job, Social_media, Vacancy, Aplication
from .serializers import CategorySerializer, ProductSerializer, JobSerializer, Social_mediaSerializer
from .serializers import VacancySerializer, AplicationSerializer


class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class JobListAPIView(ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class Social_mediaListAPIView(ListCreateAPIView):
    queryset = Social_media.objects.all()
    serializer_class = Social_mediaSerializer

class Social_mediaDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Social_media.objects.all()
    serializer_class = Social_mediaSerializer


class VacancyListAPIView(ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer



class AplicationListAPIView(ListCreateAPIView):
    queryset = Aplication.objects.all()
    serializer_class = AplicationSerializer

class AplicationDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Aplication.objects.all()
    serializer_class = AplicationSerializer


