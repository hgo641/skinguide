# Generated by Django 3.1.2 on 2020-10-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin', '0002_auto_20201015_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=100, null=True),
        ),
    ]