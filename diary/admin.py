from django.contrib import admin
from .models import ColdEntry,Diary

# Register your models here.

admin.site.register([ColdEntry,Diary])