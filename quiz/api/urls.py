from django.urls import path
from .views import QuizCreateView, QuizListView, QuizDetailView

urlpatterns = [
    path('quizzes/', QuizListView.as_view(), name='quiz_list'),
    path('quizzes/create/', QuizCreateView.as_view(), name='quiz_create'),
    path('quizzes/<int:id>/', QuizDetailView.as_view(), name='quiz_detail'),
]
