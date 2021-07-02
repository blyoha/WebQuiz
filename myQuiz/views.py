from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Answer, Question

from .services.results_calculation import calculate_results


def index(request):
    # Render certain form
    # questions = Question.objects.all()

    for obj in Question.objects.all():
        for ans in obj.answer_set.all():
            ans.is_checked = False
            ans.save()

    return render(request, 'myQuiz/index.html')


def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    checked_ans = list()
    try:
        for a in request.POST.getlist('ans'):
            checked_ans.append(q.answer_set.get(pk=a))
            # current_a = q.answer_set.get(pk=request.POST.getlist('ans'))
    except (KeyError, Answer.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'myQuiz/questionLayout.html', {
            'question': q,
            'error_message': "Пожалуйста, выберите ответ.",
        })
    else:
        for a in checked_ans:
            a.is_checked = True
            a.save()

        if q.id == 5:
            return HttpResponseRedirect(reverse('myQuiz:results'))
        return HttpResponseRedirect(reverse('myQuiz:question', args=(question_id+1, )))


def question(request, question_id):
    button_val = 'Далее'
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'myQuiz/questionLayout.html', {'question': q, })


def results(request):
    percent: int = calculate_results()  # Gets percentage of right answers
    return render(request, 'myQuiz/results.html', {'right_answers': percent})
