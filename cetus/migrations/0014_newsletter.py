# Generated by Django 3.1.1 on 2023-03-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cetus', '0013_requirnment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
