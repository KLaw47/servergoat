from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bagelapi.models import Recipe, User

class RecipeView(ViewSet):

    def retrieve(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        serializer RecipeSerializer(recipe)
        return Response(serializer.data)

    def list(self, request):

        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def create(self, request):

        recipe = Recipe.objects.create(
            
        )
