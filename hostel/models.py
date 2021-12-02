from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
    related_name='user_profile')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    description = models.TextField(blank=True)
    full_name = models.CharField(max_length=264, blank=True)
    dob = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    class Meta:
        db_table = "user_profile"
class Student(models.Model):
    author = models.ForeignKey(User, blank=True, related_name='student', on_delete=models.SET_NULL),
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    section = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)  
    room_no = models.IntegerField()
    

    def __str__(self):
        return f'{self.email},{self.name}'

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='post_images')
    caption = models.CharField(max_length=264, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['-upload_date', ]

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_post' )   
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker')   
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
         return '{} : {}'.format(self.user, self.post)     

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    category = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=200, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    Status = (
        ("Pending", 'Pending'),
        ("Delivered", 'Delivered'),
        ("Out of delivery", 'Out of delivery'),
    )
    customer_id = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    product_id = models.ManyToManyField(Product)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=Status)
    def __str__(self):
        return self.customer_id.author + " "+ self.customer_id.email         

