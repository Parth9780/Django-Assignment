# Generated by Django 4.2 on 2024-10-04 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsubcat',
            name='product_image',
            field=models.FileField(upload_to=''),
        ),
    ]
