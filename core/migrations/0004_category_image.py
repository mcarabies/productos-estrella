# Generated by Django 5.1.1 on 2024-09-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.URLField(blank=True, max_length=350, null=True, verbose_name='Imagen de Categoria'),
        ),
    ]
