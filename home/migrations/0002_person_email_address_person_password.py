# Generated by Django 4.2.7 on 2023-12-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email_address',
            field=models.EmailField(default='salut@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default=123, max_length=30),
        ),
    ]
