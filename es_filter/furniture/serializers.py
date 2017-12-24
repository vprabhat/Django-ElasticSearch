from rest_framework import serializers
from .models import Sofa, Bed, Dining

class SofaSerializerES(serializers.ModelSerializer):
    _id = serializers.CharField(source='id', read_only=True)
    class Meta:
        model = Sofa
        exclude = ('id',)


class BedSerializerES(serializers.ModelSerializer):
    _id = serializers.CharField(source='id', read_only=True)
    class Meta:
        model = Bed
        exclude = ('id',)


class DiningSerializerES(serializers.ModelSerializer):
    _id = serializers.CharField(source='id', read_only=True)
    class Meta:
        model = Dining
        exclude = ('id',)