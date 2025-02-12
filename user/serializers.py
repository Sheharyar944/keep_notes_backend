from django.contrib.auth.models import User
from rest_framework import serializers
from notes.serializers import NotesSerializer
from django.core.validators import RegexValidator

class UserSerializer(serializers.ModelSerializer):
    notes = NotesSerializer(many=True, read_only=True)

    password = serializers.CharField(
        write_only=True,
        min_length=8,
        validators=[
            RegexValidator(
                regex="^(?=.*[a-zA-Z])(?=.*\d)[A-Za-z\d]+$",
                message="Password must be alphanumeric (contain both letters and numbers).",
            )
        ]
    )


    class Meta:
        model= User
        fields= ['url','id', 'username', 'email', 'password', 'notes']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True, 'allow_blank':False},
            'username': {'min_length': 4},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

        

