# Generated by Django 4.1.7 on 2023-05-13 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_remove_categorie_pre_remove_categorie_pred'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='pred',
            field=models.CharField(default='', max_length=255),
        ),
    ]