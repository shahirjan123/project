# Generated by Django 4.2.4 on 2023-09-02 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0004_productbrand_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/products', verbose_name='تصویر محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=200, unique=True, verbose_name='عنوان در url'),
        ),
    ]
