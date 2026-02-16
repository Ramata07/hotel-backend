from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class CustomUserCreateSerializer(UserCreateSerializer):
    """Serializer pour l'enregistrement
    
    RESPECTE LES EXIGENCES:
    - Enregistrement: username, email, password, password2
    - Connexion: username, password
    """
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    re_password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        # ✅ ACCEPTER: username, email, password, re_password
        # re_password vient de password2 du formulaire React
        fields = ('id', 'username', 'email', 'password', 're_password')
        read_only_fields = ('id',)

    def validate(self, attrs):
        """Vérifier que password et re_password correspondent"""
        if attrs['password'] != attrs['re_password']:
            raise serializers.ValidationError(
                {"password": "Les mots de passe doivent correspondre."}
            )
        return attrs

    def create(self, validated_data):
        """Supprimer re_password avant de créer l'utilisateur"""
        validated_data.pop('re_password', None)
        user = User.objects.create_user(**validated_data)
        return user


class CustomUserSerializer(UserSerializer):
    """Serializer pour afficher les infos utilisateur (GET /auth/users/me/)"""
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email')
        read_only_fields = ('id',)