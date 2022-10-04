from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from .models import Category, QuestionAnswer
from .serializers import CategorySerializer, QuestionAnswerSerializer, QuestionAnswerSerializerPUT


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerListCreateAPIView(ListCreateAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer

    def get_queryset(self):
        queryset = self.queryset
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        question = self.request.query_params.get('question')
        if question:
            queryset = queryset.filter(question__icontains=question)
        return queryset.order_by('-importance')


class QuestionAnswerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializerPUT


