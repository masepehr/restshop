# Generated by Django 3.0.4 on 2020-03-24 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20200217_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_path',
            field=models.ImageField(upload_to='products/'),
        ),
    ]
