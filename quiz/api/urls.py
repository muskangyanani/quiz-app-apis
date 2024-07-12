from django.urls import path
from .views import QuizCreateView, QuizListView

urlpatterns = [
    path('quizzes/', QuizListView.as_view(), name='quiz_list'),
    path('quizzes/create/', QuizCreateView.as_view(), name='quiz_create'),
]
