from django.contrib import admin

from .models import Category, Product

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug':('title', )}
    
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','description','slug','prices', 'created', 'updated', 'in_stalk']
    list_filter = ['in_stalk', 'in_active']
    list_editable = ['prices', 'in_stalk']
    prepopulated_fields = {'slug':('title', )}