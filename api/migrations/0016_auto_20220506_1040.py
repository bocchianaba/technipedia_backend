# Generated by Django 3.2.13 on 2022-05-06 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='added_value',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='difference_with_existence',
            field=models.TextField(blank=True, verbose_name='Difference with existents products and services'),
        ),
        migrations.AddField(
            model_name='product',
            name='fabrication_method',
            field=models.TextField(blank=True, verbose_name='Fabrication method'),
        ),
        migrations.AddField(
            model_name='product',
            name='services',
            field=models.TextField(blank=True, verbose_name='Services'),
        ),
        migrations.AlterField(
            model_name='product',
            name='exportation_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='exportation value in dollars'),
        ),
        migrations.AlterField(
            model_name='product',
            name='importation_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='importation value in dollars'),
        ),
    ]
