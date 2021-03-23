from django.db import models

CATEGORY=(
            ('vector','vector'),
            ('raster','raster'),
            ('ui','ui'),
            ('printing','printing')
        )

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    subject=models.TextField()
    message=models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):
    name=models.CharField(max_length=300)
    image=models.TextField()
    comment=models.TextField()

    def __str__(self):
        return self.name
    

class Project(models.Model):
    name=models.CharField(max_length=300)
    image=models.TextField()
    type=models.CharField(max_length=50)
    category=models.CharField(choices=CATEGORY,blank=True,max_length=100)

    def __str__(self):
        return self.name
    

