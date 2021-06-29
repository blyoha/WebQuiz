from django.shortcuts import render
from .models import Answer, Question


def index(request):
    # Render certain form
    return render(request, 'myQuiz/index.html')


def question(request, question_id):
    questions = Question.objects.all()
    return render(request, 'myQuiz/questionLayout.html', {'question_id': question_id})


def results(request):
    return render(request, 'myQuiz/results.html')
