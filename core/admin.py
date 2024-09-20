from django.contrib import admin
from .models import Category, Tag, Product, About, Linksocial, Productimages

# Register your models here.
# CATEGORIAS
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active')

# ETIQUETAS
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active')

# PRODUCTOS
class ImagesInstanceInLine(admin.TabularInline):
    model = Productimages
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Contenido', {
                'fields': ('title',('excerpt','content'), ('created', 'updated'),),
            }
        ),
        (
            'Amazon',{
                'fields': (('url_amazon','url_afiliado_amazon'),)
            }    
        ),
       
    )
    readonly_fields = ('created', 'updated')
    list_display = ('published', 'title', 'category', 'created' )
    ordering = ('published','-created', 'title')
    search_fields = ('title',)
    inlines = [ImagesInstanceInLine]
    #@admin.display(description ='url')
    #def images(self):
     #   images_list = []
      #  images_list = Productimages.objects.filter(Product)
       # print(images_list)
        #return images_list

# ACERCA DE NOSOTROS
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('description',)

# REDES SOCIALES
@admin.register(Linksocial)
class LinksocialAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'url')
    search_fields = ('title',)

# IMAGENES DE PRODUCTOS
@admin.register(Productimages)
class ProductimagesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('product', 'url')
