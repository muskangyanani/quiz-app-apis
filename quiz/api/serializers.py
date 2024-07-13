from rest_framework import serializers
from .models import Quiz, Question, Option

class OptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Option
    fields = ['id', 'text', 'is_correct']

class QuestionDetailSerializer(serializers.ModelSerializer):
  options = OptionSerializer(many=True, read_only=True)
  
  class Meta:
    model = Question
    fields = ['id', 'question_text', 'options','no_of_questions', 'correct_answer']

class QuestionSerializer(serializers.ModelSerializer):
  options = OptionSerializer(many=True)

  class Meta:
    model = Question
    fields = ['id', 'text', 'options']

class QuizSerializer(serializers.ModelSerializer):
  class Meta:
    model = Quiz
    fields = ['id', 'name', 'time_limit', 'no_of_questions']


class QuizDetailSerializer(serializers.ModelSerializer):
  questions = QuestionSerializer(many=True)
  no_of_questions = serializers.IntegerField(read_only=True)

  class Meta:
    model = Quiz
    fields = ['id', 'name', 'no_of_questions', 'time_limit', 'questions']

  def create(self, validated_data):
    questions_data = validated_data.pop('questions')
    quiz = Quiz.objects.create(**validated_data)
    print(quiz.id)
    for question_data in questions_data:
        options_data = question_data.pop('options')
        question = Question.objects.create(quiz=quiz, **question_data)
        for option_data in options_data:
            Option.objects.create(question=question, **option_data)
    quiz.no_of_questions = quiz.questions.count()
    quiz.save()
    return quiz

  def update(self, instance, validated_data):
    questions_data = validated_data.pop('questions')
    instance.name = validated_data.get('name', instance.name)
    instance.time_limit = validated_data.get('time_limit', instance.time_limit)
    instance.save()

    for question_data in questions_data:
      options_data = question_data.pop('options')
      question_id = question_data.get('id')
      if question_id:
        question = Question.objects.get(id=question_id, quiz=instance)
        question.text = question_data.get('text', question.text)
        question.save()
        for option_data in options_data:
          option_id = option_data.get('id')
          if option_id:
            option = Option.objects.get(id=option_id, question=question)
            option.text = option_data.get('text', option.text)
            option.is_correct = option_data.get('is_correct', option.is_correct)
            option.save()
          else:
            Option.objects.create(question=question, **option_data)
      else:
          question = Question.objects.create(quiz=instance, **question_data)
          for option_data in options_data:
              Option.objects.create(question=question, **option_data)
    instance.no_of_questions = instance.questions.count()
    instance.save()
    return instance