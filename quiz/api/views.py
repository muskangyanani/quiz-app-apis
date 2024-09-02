from rest_framework import generics
from .models import Quiz
from .serializers import QuizSerializer, QuizDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

class QuizCreateView(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizDetailSerializer

class QuizListView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizDetailView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizDetailSerializer
    lookup_field = 'id'

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_quizzes(request):
    quizzes = Quiz.objects.filter(created_by=request.user)
    print(quizzes)
    serializer = QuizSerializer(quizzes, many=True)
    return Response(serializer.data)