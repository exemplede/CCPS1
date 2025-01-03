from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    fullname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname'] 

    def __str__(self):
        return self.email
    
    def has_module_perms(self, obj=None):
        return True
    
    def has_perm(self, perm, obj=None):
        return True

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, related_name='actus', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated_at']
        
    def __str__(self):
        if len(self.content) <= 200:
            return self.content
        
        
        return self.content[:200]+'...'
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated_at']
        
    def __str__(self):
        if len(self.content) <= 200:
            return self.content
        
        
        return self.content[:200]+'...'

    
class SiteVisit(models.Model):
        created_at = models.DateTimeField(auto_now=True)
    
def __str__(self):
        return f"Total Site Visits: {self.count}"
    
    
class Image(models.Model): 
    img = models.ImageField(upload_to='images', blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="images", blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images", blank=True, null=True)
    caption = models.CharField(max_length=100, blank=True, null=True) # une petite description de ce que represente l'image