from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bagelapi.models import Yeast_Type

class YeastTypeView(ViewSet):

    def retrieve(self, request, pk):

        yeast_type = Yeast_Type.objects.get(pk=pk)
        serializer = YeastTypeSerializer(yeast_type)
        return Response(serializer.data)

    def list(self, request):

        yeast_type = Yeast_Type.objects.all()
        serializer = YeastTypeSerializer(yeast_type, many=True)
        return Response(serializer.data)

class YeastTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yeast_Type
        fields = ('id', 'yeast_type', 'ounces', 'grams')
