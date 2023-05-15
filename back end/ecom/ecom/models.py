from django.db import models
from django.conf import settings

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    slug = models.CharField(max_length=255,default="")

class Produit(models.Model):
    nom= models.CharField(max_length=255,default="")
    description= models.CharField(max_length=255,default="")
    prix = models.CharField(max_length=255, default="")
    promotionPrix = models.FloatField(default= 0)
    image = models.CharField(max_length=1000, null= True,default="")
    categorie = models.ForeignKey(Categorie,null= True ,on_delete= models.CASCADE)

class Commande(models.Model):
    products = models.ManyToManyField(Produit)
    confirmation = models.BooleanField(default=False)
    isdelivered = models.BooleanField(default=False)
    prixTotal = models.FloatField(default=0)
    client = models.ForeignKey(settings.AUTH_USER_MODEL ,null= True , on_delete= models.CASCADE)




