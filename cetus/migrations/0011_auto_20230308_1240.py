# Generated by Django 3.1.1 on 2023-03-08 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cetus', '0010_brochure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brochure',
            name='pdf',
            field=models.FileField(upload_to=''),
        ),
    ]
