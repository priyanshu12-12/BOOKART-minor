from django.db import models


# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.username


class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=1000)
    img=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
    

class Requirments(models.Model):
    name=models.CharField(max_length=200)
    number=models.IntegerField()
    bookname=models.CharField(max_length=100)
    edition=models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.bookname