# Generated by Django 3.1.1 on 2023-02-18 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cetus', '0005_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Message',
            field=models.CharField(max_length=500),
        ),
    ]
