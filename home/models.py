from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phoneno=models.IntegerField()
    subject=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=500)

    def __str__(self):
        return self.name
class Plansdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=40)
    email=models.EmailField()
    phoneno=models.IntegerField()
    plan=models.CharField(max_length=50)
    sdate=models.DateField()
    duration=models.CharField(max_length=50)
    payment=models.CharField(max_length=40)
    
    def __str__(self):
        return self.email
class Class(models.Model):
    title=models.CharField(max_length=60)
    img=models.ImageField(upload_to='class',blank=True,null=True)
    description=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.title