from django.db import models
import  PIL 
from PIL import Image
from datetime import datetime
import datetime



class Category(models.Model):
    CategoryName=models.CharField(max_length=200)
    Image=models.ImageField(default="https://cdn.wpmeducation.com/53544f/97c04745fa/default.jpg")
    
    def __str__(self):
        return self.CategoryName

class Product(models.Model):
    ModelNo=models.CharField(max_length=200)
    ProductImage=models.ImageField(default="https://cdn.wpmeducation.com/53544f/97c04745fa/default.jpg")
    Category=models.ForeignKey("Category", on_delete=models.SET_DEFAULT,default=1)         

    def __str__(self):
        return self.ModelNo

class Contact(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Subject=models.CharField(max_length=500)
    Message=models.CharField(max_length=500)

    def __str__(self):
        return self.Email        
    
class Requirnment(models.Model):
    Name=models.CharField(max_length=200)
    Company=models.CharField(max_length=200)    
    Designation=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    City=models.CharField(max_length=200)
    Pincode=models.CharField(max_length=200)
    State=models.CharField(max_length=200)
    Country=models.CharField(max_length=200)
    Mobile=models.CharField(max_length=200)
    Telephone=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Modelno=models.CharField(max_length=200)
    date = models.DateField(("Date"), default=datetime.date.today)



    def __str__(self):
        return self.Name


class brochure(models.Model):
    name=models.CharField(max_length=200)
    image= models.ImageField( default="https://cdn.wpmeducation.com/53544f/97c04745fa/default.jpg") 
    pdf= models.FileField()
        
    def __str__(self):
        return self.name         


class Register(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)

    def __str__(self):
        return self.Email        

class newsletter(models.Model):
    mail=models.EmailField()
    
    def __str__(self):
        return self.mail        

class image(models.Model):
    name=models.CharField(max_length=200)
    image= models.ImageField( default="https://cdn.wpmeducation.com/53544f/97c04745fa/default.jpg") 
        
    def __str__(self):
        return self.name         
