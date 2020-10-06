from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class classsm(models.Model):
    tid = models.ForeignKey(User, on_delete=models.CASCADE)
    section=models.CharField(max_length=2)
    password=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class classsj(models.Model):
    sid = models.ForeignKey(User, on_delete=models.CASCADE)
    clid = models.ForeignKey(classsm, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False,auto_now = False,default = datetime.now(),blank = True)

class work(models.Model):
    wtype=models.CharField(max_length=50)

class classwork(models.Model):
    clid = models.ForeignKey(classsm, on_delete=models.CASCADE)
    wtype = models.ForeignKey(work, on_delete = models.CASCADE)
    wname = models.TextField()
    filess = models.FileField(null=True)

    def delete(self, *args, **kwargs):
        self.filess.delete()
        super().delete(*args, **kwargs)

class submit(models.Model):
    cwid = models.ForeignKey(classwork, on_delete=models.CASCADE)
    sid = models.ForeignKey(User, on_delete=models.CASCADE)
    stext = models.TextField()
    sfile = models.FileField(null=True)
    score = models.IntegerField(default = 0)
    def delete(self, *args, **kwargs):
        self.sfile.delete()
        super().delete(*args, **kwargs)

class qnas(models.Model):
    question = models.TextField()
    sid = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField(default="No Answer Yet")
    subject=models.CharField(max_length=50,null=True)    
    date = models.DateTimeField(auto_now_add=False,auto_now = False,default = datetime.now(),blank = True)
