from django.db import models

class PageVisit(models.Model):
    ##db->table
    #id -> primary key -> auto incrementing integer-> 1,2,3,4,5
    path = models.TextField(blank=True, null=True) #column -> string -> blank and null allowed
    timestamp = models.DateTimeField(auto_now_add=True) #column -> datetime -> auto set to now when created