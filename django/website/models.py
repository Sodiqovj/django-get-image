from django.db import models

class Car(models.Model):
    text1 = models.CharField(max_length=50)
    text2 = models.CharField(max_length=50)
    text3 = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    emblem = models.CharField(max_length=70)
    
    def __str__(self):
        return self.login
    
class Imgs(models.Model):
    
    text = models.CharField(max_length=100)
    image = models.ImageField()
    
    def __str__(self):
        return self.text
    