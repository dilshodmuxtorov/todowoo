from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
class TodoModel(models.Model):
    title = models.CharField(max_length=65,default= "")
    memo = models.TextField(default = "")
    important = models.BooleanField(default = False)
    completed = models.BooleanField(default = False)
    completed_time = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,default=None,null=True)


    def __str__(self) -> str:
        return self.title
    
