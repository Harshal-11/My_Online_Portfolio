from django.db import models

# Create your models here.
class Intro(models.Model):
    aboutme_image = models.ImageField(upload_to="static/aboutme/intro")
    aboutme_title = models.TextField(max_length=30)
    aboutme_text = models.TextField(max_length=1000)

    def __str__(self):
        return self.aboutme_title

class Gallery(models.Model):
    pic1 = models.ImageField(upload_to="static/aboutme/gallery")
    pic1_text = models.TextField()
    pic2 = models.ImageField(upload_to="static/aboutme/gallery")
    pic2_text = models.TextField()
    pic3 = models.ImageField(upload_to="static/aboutme/gallery")
    pic3_text = models.TextField()