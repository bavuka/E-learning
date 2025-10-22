from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import signals
from embed_video.fields import EmbedVideoField  #>pip install django-embed-video to add video field install this app and add it tio settings
# Create your models here.

class User(AbstractUser):
    options=(("student","student"),("instructor","instructor"))
    role= models.CharField(max_length=100,choices=options,default="student")

class InstructorProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="instrutor")
    profile_pic=models.ImageField(upload_to="images",null=True,blank=True,default="images/prof.jpg")
    expertise=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.user.username

def create_prof(sender,instance,created,**kwargs):
    if created and instance.role=="instructor":
        InstructorProfile.objects.create(user=instance)
signals.post_save.connect(create_prof,User)        


class Category(models.Model):
    category_name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.category_name    
    
class Course(models.Model):
    owner=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="owner")
    title=models.CharField(max_length=100)
    description=models.TextField()
    category=models.ManyToManyField(Category,related_name="category")
    image=models.ImageField(upload_to="images",null=True,blank=True,default="images/def.png")
    price=models.DecimalField(max_digits=5,decimal_places=2)
    def __str__(self):
        return self.title