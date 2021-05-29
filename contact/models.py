from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class ContactForm(models.Model):
    name = models.TextField(max_length = 50)
    email = models.TextField(max_length = 100)
    message = models.TextField()
    post_date = models.DateField()
    
    def __str__(self):
        return self.name + " Contacted you on : " + str(self.post_date)
