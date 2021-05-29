# Generated by Django 3.2.3 on 2021-05-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='pic2',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='pic3',
        ),
        migrations.AddField(
            model_name='gallery',
            name='pic_text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='pic1',
            field=models.ImageField(default='', upload_to='static/aboutme/gallery'),
        ),
    ]
