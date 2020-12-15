from django.contrib import admin

# Register your models here.
from .models import blogcomment,blogpost
admin.site.register(blogpost.Post)
admin.site.register(blogcomment.Comment)