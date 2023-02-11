from django.db import models

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

class Courses(models.Model):
    name = models.CharField(max_length=100)
    duaration = models.IntegerField()

class Student(BaseModel):
    courses = models.ManyToManyField(Courses)
    major = models.CharField(max_length=100)
    cgpa = models.FloatField()
    
class Teacher(BaseModel):
    courses = models.ManyToManyField(Courses)
    experience = models.IntegerField()
    subject_expertise = models.CharField(max_length=100)

