from pereval.models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from pereval.views import *


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height',)


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter', 'spring', 'summer', 'autumn',)


class PassUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassUser
        fields = ('email', 'fam', 'name', 'otc', 'phone',)


class ImagesSerializer(serializers.ModelSerializer):
    data = serializers.URLField()

    class Meta:
        model = Images
        fields = ('data', 'title',)


class PerevalSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    status = serializers.CharField(read_only=True)
    level = LevelSerializer(allow_null=True)
    user = PassUserSerializer()
    coords = CoordsSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        fields = (
            'user',
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'coords',
            'level',
            'images',
            'add_time',
            'status',
        )