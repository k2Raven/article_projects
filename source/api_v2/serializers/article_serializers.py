from rest_framework import serializers

from api_v2.serializers.tags_serializers import TagSerializer
from webapp.models import Article

class ArticleSerializer(serializers.ModelSerializer):

    def validate(self, data):
        return super().validate(data)

    def validate_title(self, title):
        if len(title) < 5:
            raise serializers.ValidationError('Article title must be at least 5 characters')
        return title

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'author', 'tags', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            validated_data['author'] = request.user
        return super().create(validated_data)

class ArticleListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'tags')