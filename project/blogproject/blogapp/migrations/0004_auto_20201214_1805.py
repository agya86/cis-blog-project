# Generated by Django 3.1.4 on 2020-12-14 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20201214_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.CharField(max_length=200),
        ),
    ]
