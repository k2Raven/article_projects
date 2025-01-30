from rest_framework import serializers

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
