from rest_framework import serializers

from .models import BirbMeme

class BirbMemeSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = BirbMeme
        fields = '__all__'