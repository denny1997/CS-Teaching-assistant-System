from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=20)
    credits = models.IntegerField()
    sectionNumber = models.CharField(max_length=20)
    description = models.TextField(max_length=100000)

class Faculty(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    research_area = models.TextField(max_length=500)

class Teaches(models.Model):
    semester = models.CharField(max_length=20)
    faculty = models.ForeignKey('Faculty',on_delete=models.CASCADE)
    course = models.ForeignKey('Course',on_delete=models.CASCADE)