from django.db import models

class Form(models.Model):
    rollno=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    math=models.CharField(max_length=50)
    physic=models.CharField(max_length=50)
    chemistry=models.CharField(max_length=50)
    total=models.CharField(max_length=50)
    percent=models.CharField(max_length=50)

    def __str__(self):
        return self.name
