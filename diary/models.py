from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Diary(models.Model):
    diary_name=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    year=models.PositiveIntegerField()

    def save(self,*args,**kwargs):
        self.diary_name=f"{self.diary_name}-{self.year}"
        super().save(self,*args,**kwargs)

    def __str__(self):
        return self.diary_name

class ColdEntry(models.Model):
    serial_no=models.PositiveIntegerField()
    packets=models.IntegerField()
    floor=models.IntegerField()
    rank=models.CharField(max_length=3000)
    removed_packets=models.CharField(max_length=2000,default="0")
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    # Date of the day the entry removed
    imported_at=models.DateField(auto_now_add=True)
    exported_at=models.DateField(auto_now_add=True)
    incold=models.BooleanField(default=True)

    diary=models.ForeignKey(Diary,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)+'- '+str(self.created_by.username)+' '+str(self.rank)



