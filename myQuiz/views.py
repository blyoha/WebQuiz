from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Question

from .services.app_logic import calculate_results, clear_db, trace_answer


def index(request):
    clear_db()

    return render(request, 'myQuiz/index.html')


def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    trace_answer(request, q)

    if q.id == 5:
        return HttpResponseRedirect(reverse('myQuiz:results'))

    return HttpResponseRedirect(reverse('myQuiz:question', args=(question_id+1, )))


def question(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'myQuiz/question.html', {'question': q})


def results(request):
    percent: int = calculate_results()  # Gets percentage of right answers
    return render(request, 'myQuiz/results.html', {'right_answers': percent})
