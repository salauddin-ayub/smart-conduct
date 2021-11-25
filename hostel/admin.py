from django.contrib import admin
from .models import Student,UserProfile,Post,Like

# Register your models here.
admin.site.register(Student)
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Like)