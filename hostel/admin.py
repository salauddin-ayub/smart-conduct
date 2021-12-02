from django.contrib import admin
from .models import Student,UserProfile,Post,Like,Product,Order

# Register your models here.
admin.site.register(Student)
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Product)
admin.site.register(Order)