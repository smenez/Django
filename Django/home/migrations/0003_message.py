# Generated by Django 4.2.7 on 2023-12-04 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_person_email_address_person_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.TextField(max_length=2)),
                ('contenu', models.TextField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
