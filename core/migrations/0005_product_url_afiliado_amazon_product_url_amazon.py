# Generated by Django 5.1.1 on 2024-09-17 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url_afiliado_amazon',
            field=models.URLField(blank=True, max_length=350, null=True, verbose_name='Enlace Afiliado Amazon'),
        ),
        migrations.AddField(
            model_name='product',
            name='url_amazon',
            field=models.URLField(blank=True, max_length=350, null=True, verbose_name='Enlace Original Amazon'),
        ),
    ]
