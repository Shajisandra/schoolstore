from django.db import models


# Create your models here.
class school(models.Model):

    name=models.CharField(max_length=100)
    dob=models.DateField()
    age=models.TextField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    phone=models.CharField(max_length=15)
    mail=models.CharField(max_length=100)
    address=models.TextField()
    department=models.CharField(max_length=100)
    purpose=models.CharField(max_length=15)
    materials=models.CharField(max_length=15)
