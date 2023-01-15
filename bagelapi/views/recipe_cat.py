from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bagelapi.models import Recipe, Category, Recipe_Cat

class RecipeCatView(ViewSet):

    def create(self, request):

        category = Category.objects.get(pk=request.data['category_id'])
        recipe = Recipe.objects.get(pk=request.data['recipe_id'])

        recipe_cat = Recipe_Cat.objects.create(
            category=category,
            recipe = recipe
        )
        serializer = RecipeCatSerializer(recipe_cat)
        return Response(serializer.data)

    def destroy(self, request, pk):
        recipe_cat = Recipe_Cat.objects.get(pk=pk)
        recipe_cat.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class RecipeCatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe_Cat
        fields = ('id', 'category', 'recipe')
        depth = 1
