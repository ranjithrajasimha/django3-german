from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    # TYPE_CHOICES = ( ('Ad', 'Adjectives'), ('T', 'Tenses'), ('C', 'Cases'), ('Ar', 'Artikels'), ('S', 'Stories') )
    PERSON_CHOICES = (('Ranjith', 'Ranjith'), ('Rinee', 'Rinee'))
    # topic = models.CharField(max_length=32, choices=TYPE_CHOICES)
    created_by = models.CharField(max_length=32, choices=PERSON_CHOICES)
    comments = models.TextField(blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title