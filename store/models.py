from email.policy import default
from tabnanny import verbose

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(in_active=True)

class Category(models.Model):
    title = models.CharField( max_length=50, db_index=True )
    slug = models.SlugField(max_length=50, unique=True)
    
    
    class Meta:
         verbose_name_plural = 'Categories'
         
    def get_absolute_urls(self):
        return reverse("store:category_details", kwargs={"category_slug": self.slug})
    
    def __str__(self) :
        return self.title
    
    
class  Product(models.Model):
        category = models.ForeignKey('Category', related_name='product', on_delete=models.CASCADE)
        created_by = models.ForeignKey(User, related_name='product_user', on_delete=models.CASCADE)
        title = models.CharField( max_length=50)
        # author = models.CharField( max_length=50, default='admin')
        description = models.TextField(blank=True)
        image = models.ImageField( upload_to='images/', default='images/default.png')
        slug = models.SlugField(max_length=255)
        prices = models.DecimalField( max_digits=4, decimal_places=2)
        in_stalk = models.BooleanField(default=True)
        in_active = models.BooleanField(default=True)
        created = models.DateTimeField( auto_now_add=True)
        updated = models.DateTimeField(auto_now=False, null=True)
        objects = models.Manager()
        products = ProductManager()
        
        class Meta:
         verbose_name_plural = 'Products'
         ordering = ['-created']
         
        def __str__(self) :
            return self.title
            
        def get_absolute_url(self):
            return reverse("store:product_detail", kwargs={"slug": self.slug})
        
    
         
