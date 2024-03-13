from django.db import models as m 

# Create your models here.

class Category(m.Model):
    name = m.CharField(max_length = 250)
    info = m.TextField()
    def __str__(self):
        return self.name

class Product(m.Model):
    category = m.ForeignKey(Category, on_delete = m.CASCADE)
    name = m.CharField(max_length = 250)
    description = m.TextField() 
    price = m.IntegerField()
    image = m.ImageField()

    def __str__(self):
        return self.name

class Job(m.Model):
    job = m.CharField(max_length = 250)

    def __str__(self):
        return self.job

class Social_media(m.Model):
    name = m.CharField(max_length = 250)
    image = m.ImageField()
    def __str__(self):
        return self.name

class Vacancy(m.Model):
    jobs = m.ForeignKey(Job,on_delete = m.CASCADE)
    salary = m.IntegerField()  
    location = m.CharField(max_length = 250)
    longitude = m.CharField(max_length = 250)
    latitude = m.CharField(max_length = 250)

    short_description = m.TextField(blank  = True)
    description = m.TextField(blank  = True)

    def __str__(self):
        return self.latitude 
    

class Aplication(m.Model):
    APLICATION_CHOISES_FIELD = [
        (1, 'Male'),
        (2, 'Female'),
    ]
    full_name = m.CharField(max_length = 250)
    phone_number = m.IntegerField ()
    job = m.ForeignKey(Job, on_delete = m.CASCADE)
    description = m.TextField(blank  = True)
    cv  = m.FileField()
    status = m.IntegerField(choices=APLICATION_CHOISES_FIELD, default=1)

    def __str__(self):
        return self.full_name