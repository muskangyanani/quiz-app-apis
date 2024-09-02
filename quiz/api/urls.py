from django.urls import path
from .views import QuizCreateView, QuizListView, QuizDetailView, user_quizzes

urlpatterns = [
    path('quizzes/', QuizListView.as_view(), name='quiz_list'),
    path('quizzes/create/', QuizCreateView.as_view(), name='quiz_create'),
    path('quizzes/<int:id>/', QuizDetailView.as_view(), name='quiz_detail'),
    path('quizzes/user/', user_quizzes, name='user_quizzes'),

]
