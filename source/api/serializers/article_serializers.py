from django.contrib.auth import get_user_model
from rest_framework import serializers

from webapp.models import Tag, Article

User = get_user_model()

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100, required=True)
    text = serializers.CharField(max_length=1000, required=True, source='content')
    author = serializers.PrimaryKeyRelatedField(required=False, queryset=User.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def validate(self, data):
        return super().validate(data)

    def validate_title(self, title):
        if len(title) < 5:
            raise serializers.ValidationError('Article title must be at least 5 characters')
        return title

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        article = Article.objects.create(**validated_data)
        article.tags.set(tags)
        return article

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags')
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        instance.tags.set(tags)
        return instance
