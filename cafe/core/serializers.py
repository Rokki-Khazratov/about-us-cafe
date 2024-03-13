from rest_framework import serializers
from .models import Category, Product,Job, Social_media, Vacancy, Aplication

# raqamda korinishi kk emas hammasi str da korinishi kk 

# ichma ich api di qilish kerak 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','info']


class ProductSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    # category name 
    def get_product_name(self,obj):
        return obj.category.name

    class Meta:
        model = Product
        fields = ['product_name', 'name', 'description', 'price', 'image']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['job']


class Social_mediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_media
        fields = ['name','image']


class VacancySerializer(serializers.ModelSerializer):

    jobs_name = serializers.SerializerMethodField()

    def get_jobs_name(self, obj):
        return obj.jobs.job

    class Meta:
        model = Vacancy
        fields = ['jobs_name','salary', 'location', 'longitude', 'latitude', 'short_description', 'description']


class AplicationSerializer(serializers.ModelSerializer):
    job_name = serializers.SerializerMethodField()
    status_name = serializers.SerializerMethodField()

    def get_job_name(self,obj):
        return obj.job.job
    
    def get_status_name(self,obj):
        return obj.job.job

    class Meta:
        model = Aplication
        fields = ['full_name', 'phone_number', 'job_name', 'description', 'cv', 'status_name']
