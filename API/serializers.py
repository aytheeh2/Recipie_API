from django.contrib.auth.models import User
from rest_framework import serializers
from Recipie.models import Recipie, Review_or_Comment


class RecipieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipie
        fields = ('id', 'name', 'ingredients', 'cuisine',
                  'meal_type', 'created_at', 'edited_at',)


class Review_or_Comment_Serializer(serializers.ModelSerializer):
    recipe_name = serializers.CharField(
        source='recipe_id.name', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review_or_Comment
        exclude = ('created_at',)


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password',)

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return user
