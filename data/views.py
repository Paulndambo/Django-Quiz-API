from django.shortcuts import render
from django.utils.translation import gettext_lazy
from . models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import *
# Create your views here.
class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


#Random Questions
class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

# Questions from A Certain Quiz

class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        questions = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer =QuizQuestionSerializer(questions,many=True)
        return Response(serializer.data)