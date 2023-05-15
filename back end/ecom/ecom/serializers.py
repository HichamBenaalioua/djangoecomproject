from rest_framework import serializers
from .models import Categorie, Produit, Commande
from django.contrib.auth.models import User

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ("id","nom","slug")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ('id', "nom", 'description', 'prix', 'promotionPrix', 'image', 'categorie')

class CommandeSerializer(serializers.ModelSerializer):
    products = ProduitSerializer(many=True)

    class Meta:
        model = Commande
        fields = '__all__'
    
    def create(self, validated_data):
        products_data = validated_data.pop('products')
        commande = Commande.objects.create(**validated_data)
        for produit_data in products_data:
            produit = Produit.objects.get(pk=produit_data['id'])
            commande.products.add(produit)
        return commande

