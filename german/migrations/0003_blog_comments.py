# Generated by Django 3.1.1 on 2020-11-29 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('german', '0002_auto_20201122_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='comments',
            field=models.TextField(blank=True),
        ),
    ]
