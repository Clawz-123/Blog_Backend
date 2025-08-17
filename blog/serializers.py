from rest_framework import serializers
from .models import Blog


class BlogResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'author', 'content', 'created_at', 'updated_at', 'image', 'genre']
        read_only_fields = ['id', 'created_at', 'updated_at']
    

class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'summary', 'image', 'genre', 'content']
    
    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty")
        elif len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value

    def validate_summary(self, value):
        if not value:
            raise serializers.ValidationError("Summary cannot be empty")
        elif len(value) < 10:
            raise serializers.ValidationError("Summary must be at least 10 characters long.")
        return value
    
    def validate_content(self, value):
        if not value:
            raise serializers.ValidationError("Content cannot be empty")
        return value
    
    def validate_genre(self, value):
        if value not in dict(Blog.GenreChoices.choices):
            raise serializers.ValidationError("Invalid genre selected.")
        return value
    

class BlogUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'summary', 'image', 'genre', 'content']
    
    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty")
        elif len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value

    def validate_summary(self, value):
        if not value:
            raise serializers.ValidationError("Summary cannot be empty")
        elif len(value) < 10:
            raise serializers.ValidationError("Summary must be at least 10 characters long.")
        return value
    
    def validate_content(self, value):
        if not value:
            raise serializers.ValidationError("Content cannot be empty")
        return value
    
    def validate_genre(self, value):
        if value not in dict(Blog.GenreChoices.choices):
            raise serializers.ValidationError("Invalid genre selected.")
        return value
    