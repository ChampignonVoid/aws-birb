from rest_framework import serializers

from .models import BirbMeme, BirbUser


class BirbMemeSerializer(serializers.Serializer):
    meme_image = serializers.ImageField(
        required=True
    )
    description = serializers.CharField(
        max_length=128,
        required=True
    )


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150,
        style={'placeholder': 'Username', 'autofocus': True},
        required=True
    )
    first_name = serializers.CharField(
        max_length=30,
        style={'placeholder': 'Firstname'}
    )

    last_name = serializers.CharField(
        max_length=150,
        style={'placeholder': 'Lastname'}
    )

    email = serializers.EmailField(
        max_length=254,
        style={'placeholder': 'email'}
    )

    password = serializers.CharField(
        max_length=128,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    def validate_username(self, value):
        if not value:
            raise serializers.ValidationError("This field may not be blank.")
        if BirbUser.objects.filter(username=value).count() > 0:
            raise serializers.ValidationError("Username already exists")
