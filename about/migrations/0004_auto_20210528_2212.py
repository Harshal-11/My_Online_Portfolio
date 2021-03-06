# Generated by Django 3.2.3 on 2021-05-28 16:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20210528_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='pic_text',
        ),
        migrations.AddField(
            model_name='gallery',
            name='pic1_text',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='pic2',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='static/aboutme/gallery'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='pic2_text',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='pic3',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='static/aboutme/gallery'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='pic3_text',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='pic1',
            field=models.ImageField(upload_to='static/aboutme/gallery'),
        ),
    ]
