from rest_framework import serializers
from .models import Category, Product,Job, Social_media, Vacancy, Aplication

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','info']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'image']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['job']


class Social_mediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_media
        fields = ['name','image']


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['salary', 'location', 'longitude', 'latitude', 'short_description', 'description']


class AplicationSerializer(serializers.ModelSerializer):
    job_name = serializers.SerializerMethodField()

    def get_job_name(self,obj):
        return obj.job.job
    
    class Meta:
        model = Aplication
        fields = ['full_name', 'phone_number', 'job_name', 'description', 'cv', 'status']
