from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Answer, Question


def start_quiz(request):
    return render(request, 'quiz/index.html')


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        selected_choice.votes = 0
    except (KeyError, Answer.DoesNotExist):
        return render(request, 'quiz/detail.html', {
            'question': question,
            'error_message': 'Please, select a choice.',
        })
    else:
        selected_choice.votes = 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('quiz:results', args=(question.id,)))
