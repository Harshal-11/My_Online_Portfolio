# Generated by Django 3.2.2 on 2021-05-15 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('email', models.TextField(max_length=100)),
                ('message', models.TextField()),
                ('post_date_time', models.DateTimeField()),
            ],
        ),
    ]
