from django.contrib import admin
from .models import Category, Tag, Product

# Register your models here.
# CATEGORIAS
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active')
admin.site.register(Category, CategoryAdmin)

# ETIQUETAS
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active')
admin.site.register(Tag, TagAdmin)

# PRODUCTOS
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('published', 'title', 'category', 'created' )
    ordering = ('published','-created', 'title')
    search_fields = ('title',)
admin.site.register(Product, ProductAdmin)