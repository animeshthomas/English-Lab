from django.db import models


# Create your models here.

class user_details(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    phone  = models.IntegerField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=20, default='User')
    photo= models.ImageField(default='No Photo Available',upload_to='images')
    def __str__(self):
        return f'{self.first_name} {self.last_name}'





class category(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="category_images")

    def __str__(self):
        return self.name


class course(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    video=models.FileField(upload_to='videos/')
    thumbnail=models.ImageField(upload_to="thumbnails")
    cat=models.ForeignKey(category,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
    
from datetime import datetime

class course_viewed(models.Model):
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.user.reg_no} viewed {self.course.title} at {self.timestamp}"


