from django.db import models 
from django.utils.timezone import now
from .blogpost import Post

# table for create comment
class Comment(models.Model):
    blog=models.IntegerField(default=0)
    blogcomment=models.TextField()
    created_on=models.DateTimeField(default=now, editable=False)
    created_by=models.CharField(max_length=200)

    class Meta: 

        ordering = ['-created_on'] 
        db_table='comment'

    # used while managing models from terminal 

    def __str__(self): 
        return self.created_by