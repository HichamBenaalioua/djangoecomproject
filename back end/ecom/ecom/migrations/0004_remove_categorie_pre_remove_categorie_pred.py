# Generated by Django 4.1.7 on 2023-05-13 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_categorie_pred'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='pre',
        ),
        migrations.RemoveField(
            model_name='categorie',
            name='pred',
        ),
    ]
