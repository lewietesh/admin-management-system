from email.policy import default
# from time import time, timezone
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    GENDER =(
        ('Male','Male' ), ('Female', 'Female'), ('Other', 'Other'),
    )
    DISABILITY =(
        ('YES', 'YES'), ('NO', 'NO')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    firstname = models.CharField(max_length =100, null=True)
    lastname = models.CharField(max_length =100, null=True)
    date_of_birth = models.DateField(null=True)
    id_number =models.IntegerField(null=True)
    gender = models.CharField(choices =GENDER,max_length=100, null=True )
    disability = models.TextField(choices=DISABILITY, max_length=50, null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Application(models.Model):
    COURSES = (
    ('Computer Science Engineering', 'Computer Science Engineering'),
    ('Information Technology Engineering', 'Information Technology Engineering'),
    ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'),
    ('Electronics Engineering', 'Electronics Engineering'),
    )
 
    STATUS = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )
 
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    course = models.CharField(max_length=100, choices= COURSES)
    name = models.CharField(max_length=200) 
    email = models.EmailField(User, null= True ) 
    phone_no = models.IntegerField() 
    address = models.TextField(max_length=200) 
    bith_certificate = models.ImageField(upload_to="docs", null=True)
    leaving_certificate = models.ImageField(upload_to="docs", null=True)
    date_joined=models.DateField(default=timezone.now)
    Application_Status = models.TextField(max_length=100, choices=STATUS, default="Pending")
    message = models.TextField(max_length=100, default="")
 
    def __str__(self):
        return self.name
 
    
 