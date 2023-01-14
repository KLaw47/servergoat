from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bagelapi.models import Salt_Type

class SaltTypeView(ViewSet):

    def retrieve(self, request, pk):

        salt_type = Salt_Type.objects.get(pk=pk)
        serializer = SaltTypeSerializer(salt_type)
        return Response(serializer.data)

    def list(self, request):

        salt_types = Salt_Type.objects.all()
        serializer = SaltTypeSerializer(salt_types, many=True)
        return Response(serializer.data)

class SaltTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salt_Type
        fields = ('id', 'salt_type', 'teaspoons', 'grams')
