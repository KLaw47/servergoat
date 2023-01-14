from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bagelapi.models import Flour_Type

class FlourTypeView(ViewSet):

    def retrieve(self, request, pk):

        flour_type = Flour_Type.objects.all()
        serializer = FlourTypeSerializer(flour_type)
        return Response(serializer.data)

    def list(self, request):

        flour_types = Flour_Type.objects.all()
        serializer = Flour_Type(flour_types, many=True)
        return Response(serializer.data)

class FlourTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flour_Type
        fields = ('id', 'flour_type', 'cups', 'grams')
