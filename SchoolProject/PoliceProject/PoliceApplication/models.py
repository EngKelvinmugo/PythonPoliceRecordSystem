from django.db import models

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=50)
    
    def __str__(self):
        return self.name




class Report(models.Model):
    Crime=models.CharField(max_length=15)
    Suspect=models.CharField(max_length=20)
    County=models.CharField(max_length=20)
    Statement=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Crime
    
class Message(models.Model):
    name=models.CharField(max_length=15)
    email=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    message=models.CharField(max_length=100)
    
    def __str__(self):
        return f'Message: {self.name}' 


class criminal(models.Model):
    name = models.CharField(max_length=60)
    crime= models.CharField(max_length=25)
   
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='uploads/criminal/')

    def __str__(self):
        return self.name
    
    
class Offense(models.Model):
    crime= models.CharField(max_length=60)  
    criminal=models.CharField(max_length=60)
    county=models.CharField(max_length=60)
    status=models.CharField(max_length=60)
    
    def __str__(self):
        return self.crime