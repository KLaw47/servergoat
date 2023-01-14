from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bagelapi.models import Recipe, User, Flour_Type, Salt_Type, Yeast_Type

class RecipeView(ViewSet):

    def retrieve(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def list(self, request):

        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def create(self, request):
        flour_id = Flour_Type.objects.get(pk=request.data["flour_id"])
        salt_id = Salt_Type.objects.get(pk=request.data["salt_id"])
        yeast_id = Yeast_Type.objects.get(pk=request.data["yeast_id"])
        user_id = User.objects.get(pk=request.data["user_id"])

        recipe = Recipe.objects.create(
            name=request.data["name"],
            flour_id=flour_id,
            salt_id=salt_id,
            yeast_id=yeast_id,
            water=request.data["water"],
            flour_amount=request.data["flour_amount"],
            salt_amount=request.data["salt_amount"],
            yeast_amount=request.data["yeast_amount"],
            directions=request.data["directions"],
            image=request.data["image"],
            public=request.data["public"],
            user_id=user_id
        )
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def update(self, request, pk):

        flour_id = Flour_Type.objects.get(pk=request.data["flour_id"])
        salt_id = Salt_Type.objects.get(pk=request.data["salt_id"])
        yeast_id = Yeast_Type.objects.get(pk=request.data["yeast_id"])
        user_id = User.objects.get(pk=request.data["user_id"])

        recipe = Recipe.objects.get(pk=pk)
        recipe.name=request.data["name"]
        recipe.flour_id=flour_id
        recipe.yeast_id=yeast_id
        recipe.salt_id=salt_id
        recipe.water=request.data["water"]
        recipe.flour_amount=request.data["flour_amount"]
        recipe.salt_amount=request.data["salt_amount"]
        recipe.yeast_amount=request.data["yeast_amount"]
        recipe.directions=request.data["directions"]
        recipe.image=request.data["image"]
        recipe.public=request.data["public"]
        recipe.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        recipe.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'flour_id', 'salt_id', 'yeast_id', 'water', 'flour_amount', 'salt_amount', 'yeast_amount', 'directions', 'image', 'public', 'user_id')
        depth = 1
