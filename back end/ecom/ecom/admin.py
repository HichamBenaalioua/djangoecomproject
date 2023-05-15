from django.contrib import admin
from .models import Categorie, Produit, Commande


class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'confirmation', 'prixTotal', 'get_products')

    def get_products(self, obj):
        return "\n".join([p.nom for p in obj.products.all()])
    get_products.short_description = 'Liste des produits'

admin.site.register(Commande, CommandeAdmin)

admin.site.register(Categorie)
admin.site.register(Produit)