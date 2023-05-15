# Generated by Django 4.1.7 on 2023-05-13 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('prix', models.FloatField(default=0)),
                ('promotionPrix', models.FloatField(default=0)),
                ('image', models.CharField(max_length=255, null=True)),
                ('categorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation', models.BooleanField(default=False)),
                ('prixTotal', models.FloatField(default=0)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.client')),
                ('products', models.ManyToManyField(to='ecom.produit')),
            ],
        ),
    ]