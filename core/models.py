from django.db import models

# Create your models here.
# MODELO CATEGORIA
class Category (models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']
    
    def __str__(self):
        return self.name

# MODELO ETIQUETAS
class Tag (models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    
    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['name']
    
    def __str__(self):
        return self.name


# MODELO PRODUCTO
class Product(models.Model):
    title = models.CharField(max_length=120,verbose_name='Título')
    excerpt = models.TextField(max_length=300, verbose_name='Descripción Corta')
    content = models.TextField (max_length=1000, verbose_name='Descripción Larga')
    published = models.BooleanField(default=False, verbose_name='Publicado')
    #Relaciones
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    tags = models.ManyToManyField(Tag, verbose_name='Etiquetas')
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-created']
    
    def __str__(self):
        return self.title
    
    