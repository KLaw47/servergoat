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

        user_recipes = request.query_params.get('user', None)
        if user_recipes is not None:
            recipes = recipes.filter(user=user_recipes)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def create(self, request):
        flour = Flour_Type.objects.get(pk=request.data["flour_id"])
        salt = Salt_Type.objects.get(pk=request.data["salt_id"])
        yeast = Yeast_Type.objects.get(pk=request.data["yeast_id"])
        user = User.objects.get(pk=request.data['user_id'])
        water_amount = float(request.data["water"])
        flour_grams = flour.grams
        yeast_grams = yeast.grams
        salt_grams = salt.grams
        total_salt = float(request.data["salt_amount"]) * salt_grams
        total_flour = float(request.data["flour_amount"]) * flour_grams
        total_yeast = float(request.data["yeast_amount"]) * yeast_grams

        recipe = Recipe.objects.create(
            name=request.data["name"],
            flour=flour,
            salt=salt,
            yeast=yeast,
            water=str(water_amount * 240),
            flour_amount=total_flour,
            salt_amount=total_salt,
            yeast_amount=total_yeast,
            directions=request.data["directions"],
            image=request.data["image"],
            public=request.data["public"],
            user=user,
        )
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def update(self, request, pk):

        flour = Flour_Type.objects.get(pk=request.data["flour_id"])
        salt = Salt_Type.objects.get(pk=request.data["salt_id"])
        yeast = Yeast_Type.objects.get(pk=request.data["yeast_id"])
        user = User.objects.get(pk=request.data["user_id"])

        recipe = Recipe.objects.get(pk=pk)
        recipe.name=request.data["name"]
        recipe.flour=flour
        recipe.yeast=yeast
        recipe.salt=salt
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
        fields = ('id', 'name', 'flour', 'salt', 'yeast', 'water', 'flour_amount', 'salt_amount', 'yeast_amount', 'directions', 'image', 'public', 'user')
        depth = 1
