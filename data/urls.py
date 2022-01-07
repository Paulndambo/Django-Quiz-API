from django.urls import path
from . views import Quiz, QuizQuestion,RandomQuestion

urlpatterns = [
    path("", Quiz.as_view(), name="quiz"),
    path("random-question/<str:topic>/", RandomQuestion.as_view(), name="random-question"),
    path("quiz-questions/<str:topic>/", QuizQuestion.as_view(), name="quiz-questions"),
]
