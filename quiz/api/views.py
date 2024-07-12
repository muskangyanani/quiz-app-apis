from rest_framework import generics
from .models import Quiz
from .serializers import QuizSerializer, QuizDetailSerializer

class QuizCreateView(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizDetailSerializer

class QuizListView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
