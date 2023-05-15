from rest_framework import generics
from .models import Categorie,Produit,Commande
from .serializers import CategorieSerializer,UserSerializer, ProduitSerializer,CommandeSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.views.generic import ListView

class CategorieList(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class CategorieDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProduitList(generics.ListCreateAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class CommandeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

class CommandeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

@method_decorator(csrf_exempt, name='dispatch')
class CheckUserPasswordView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'exists': False})

        if user.check_password(password):
            return JsonResponse({'exists': True, 'user_id': user.id})
        else:
            return JsonResponse({'exists': False})

@method_decorator(csrf_exempt, name='dispatch')        
class ProduitByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProduitSerializer

    def get_queryset(self):
        categorie_id = self.kwargs['categorie_id']
        return Produit.objects.filter(categorie_id=categorie_id)