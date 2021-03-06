# Generated by Django 3.0.4 on 2020-03-25 11:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200325_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='verified'),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='verification_uuid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Unique Verification UUID'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
    ]
