from django.db import models
import mongoengine

class Course(models.Model):
    name = models.CharField(max_length=20)
    credits = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.TextField(max_length=100000)

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    title = models.TextField(max_length=500)

class Teaches(models.Model):
    semester = models.CharField(max_length=20)
    faculty = models.ForeignKey('Faculty',on_delete=models.CASCADE)
    course = models.ForeignKey('Course',on_delete=models.CASCADE)

class course(mongoengine.Document):
    classId = mongoengine.StringField(max_length=16)
    name = mongoengine.StringField(max_length=16)
    semester = mongoengine.StringField(max_length=16)
    instructor = mongoengine.StringField(max_length=16)
    enrollNumber = mongoengine.IntField(default=0)

class faculty(mongoengine.Document):
    name = mongoengine.StringField(max_length=16)
    areas = mongoengine.ListField()