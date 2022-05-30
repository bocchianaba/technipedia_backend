# Generated by Django 3.2.13 on 2022-05-02 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profil_img',
            field=models.FileField(default=False, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=False, max_length=30, unique=True),
        ),
    ]
