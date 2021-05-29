from django.db import models

# Create your models here.

class Hero(models.Model):
    imageUrl = models.ImageField(upload_to="static/home/hero")
    heroTitle = models.TextField(max_length=50)
    heroText = models.TextField(max_length=500)

    def __str__(self):
        return self.heroTitle
    
class Testimonial(models.Model):
    testimonial_imageUrl = models.ImageField(upload_to="static/home/testimonials")
    testimonial_text = models.TextField(max_length=10000)
    testimonial_person_name = models.TextField(max_length=30)
    testimonial_person_designation = models.TextField(max_length=30)

    def __str__(self):
        return self.testimonial_person_name
    

    
    