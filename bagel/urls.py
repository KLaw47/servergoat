"""serverbagel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from bagelapi.views import register_user, check_user
from bagelapi.views import RecipeView, YeastTypeView, SaltTypeView, FlourTypeView, UserView, CategoryView, RecipeCatView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'recipes', RecipeView, 'recipe')
router.register(r'yeast_types', YeastTypeView, 'yeast_type')
router.register(r'salt_types', SaltTypeView, 'salt_type')
router.register(r'flour_types', FlourTypeView, 'flour_type')
router.register(r'categories', CategoryView, 'category')
router.register(r'recipe_categories', RecipeCatView, 'recipe_cat')
router.register(r'users', UserView, 'user')


urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
