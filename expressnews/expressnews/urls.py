from django.contrib import admin
from django.urls import path
from newsAPI.views import ListNewsView,getfavourite,getfavouritenews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)
from restauth.views import ModsView, register,current_user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/news/', ListNewsView.as_view()),
   # path('api/newsave/', ListSaveNewsView.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Submit your refresh token to this path to obtain a new access token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Return 'Mods' model objects
    path('mods/', ModsView.as_view(), name='mods_view'),
    # Register a new user
    path('register/', register, name='register_view'),
    # user details
    path('userdetails/',current_user,name='userdetails'),
    # post saved news by user
    path('favourite/', getfavourite, name='favourite_post'),
    # get saved news by user
    path('getfavourite/', getfavouritenews, name='favourite_news'),
]
