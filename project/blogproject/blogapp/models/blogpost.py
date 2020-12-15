from django.db import models 
from django.utils.timezone import now
from django.contrib.auth.models import User

#table for BlogPost table

class Post(models.Model):
    title=models.CharField(max_length=200, unique=True)
    content=models.TextField()
    author=models.CharField(max_length=20,default='')
    updated_on = models.DateTimeField(default=now, editable=False) 
    created_on = models.DateTimeField(default=now, editable=False)
    likes=models.IntegerField(default=0)

    class Meta: 

        ordering = ['-created_on'] 
        db_table='post'

    # used while managing models from terminal 

    def __str__(self): 
        return self.title