from django.db import models as m 

# Create your models here.

class Category(m.Manager):
    name = m.CharField(max_length = 250)
    
    def __str__(self):
        return self.name
    

class Product(m.Model):
    # category
    name = m.CharField(max_length = 250)
    #description = 
    price = m.IntegerField
    image = m.ImageField

    def __str__(self):
        return self.name

class Social_media(m.Model):
    #icon
    #link
    name = m.CharField(max_length = 250)

    def __str__(self):
        return self.name

class Vacancy(m.Model):
    #job
    salary = m.IntegerField()  
    location = m.CharField(max_length = 250)
    longitude = m.CharField(max_length = 250)
    latitude = m.CharField(max_length = 250)

    #short_description = 
    #description

    def __str__(self):
        return self.salary