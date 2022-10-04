from django.urls import path

from . import views


urlpatterns = [
    path('categorys/', views.CategoryListCreateAPIView.as_view()),
    path('categorys/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('questions/', views.QuestionAnswerListCreateAPIView.as_view()),
    path('questions/<int:pk>/', views.QuestionAnswerRetrieveUpdateDestroyAPIView.as_view()),
]

