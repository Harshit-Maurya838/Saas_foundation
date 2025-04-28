from django.db import models

# Create your models here.

class PageVisit(models.Model):
    # db -> table
    # id -> primary key -> autofield -> 1,2,3,4
    page = models.TextField(null=True, blank=True) #col
    timestamp = models.DateTimeField(auto_now_add=True) #col