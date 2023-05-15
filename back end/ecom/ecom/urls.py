from django.contrib import admin
from django.urls import path
from .views import CategorieList , CategorieDetails, UserListCreateAPIView, ProduitList,CommandeListCreateAPIView,UserDetails,CommandeDetails,CheckUserPasswordView,ProduitByCategoryAPIView
from .views2 import scrape
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorie/', CategorieList.as_view(), name='listcreate'),
    path('categorie/<int:pk>/', CategorieDetails.as_view(), name='retrievedestroy'),
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetails.as_view(), name='user-details'),
    path('produits/', ProduitList.as_view(), name='produits-list-create'),
    path('commande/', CommandeListCreateAPIView.as_view(), name='commande-list-create'),
    path('commande/<int:pk>/', CommandeDetails.as_view(), name='commande-details'),
    path('check-user-password/', CheckUserPasswordView.as_view(), name='check_user_password'),
    path('productsbycategory/<int:categorie_id>/', ProduitByCategoryAPIView.as_view(), name='products by category'),

    path('scrape/<str:category>/', scrape, name='scrape'),
]

urlpatterns += staticfiles_urlpatterns()