from rest_framework import serializers

from .models import Category, QuestionAnswer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = ['id', 'question', 'answer', 'short_answer', 'importance', 'category']


class QuestionAnswerSerializerPUT(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = "__all__"
