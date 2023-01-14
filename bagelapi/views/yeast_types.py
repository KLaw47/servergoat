from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bagelapi.models import Yeast_Type

class SaltTypeView(ViewSet):

    def retrieve(self, request, pk):

        yeast_type = Yeast_Type.objects.get(pk=pk)
        serializer = SaltTypeSerializer(yeast_type)
        return Response(serializer.data)

    def list(self, request):

        yeast_type = Yeast_Type.objects.all()
        serializer = SaltTypeSerializer(yeast_type, many=True)
        return Response(serializer.data)

class SaltTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yeast_Type
        fields = ('id', 'yeast_type', 'ounces', 'grams')
