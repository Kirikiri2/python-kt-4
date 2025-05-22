from django.contrib import admin
from .models import BlogPost, Entry

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Entry)