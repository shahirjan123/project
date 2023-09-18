# Generated by Django 4.2.4 on 2023-09-17 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0002_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان بنر')),
                ('url', models.URLField(blank=True, max_length=400, null=True, verbose_name='آدرس بنر')),
                ('image', models.ImageField(upload_to='images/banners', verbose_name='تصویر بنر')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
                ('position', models.CharField(choices=[('product_list', 'صفحه لیست محصولات'), ('product_detail', 'صفحه ی جزییات محصولات'), ('about_us', 'درباره ما')], max_length=200, verbose_name='جایگاه نمایشی')),
            ],
            options={
                'verbose_name': 'بنر تبلیغاتی',
                'verbose_name_plural': 'بنرهای تبلیغاتی',
            },
        ),
    ]
