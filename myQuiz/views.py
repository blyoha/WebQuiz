from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Answer, Question


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
    try:
        current_a = q.answer_set.get(pk=request.POST['ans'])
    except (KeyError, Answer.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'myQuiz/questionLayout.html', {
            'question': q,
            'error_message': "Пожалуйста, выберите ответ.",
        })
    else:
        current_a.is_checked = True
        current_a.save()
        return HttpResponseRedirect(reverse('myQuiz:question', args=(question_id+1,)))
        # return render(request, 'myQuiz/questionLayout.html', {'question': q, 'question_id': question_id})


def question(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'myQuiz/questionLayout.html', {'question': q})


def results(request):
    return render(request, 'myQuiz/results.html')
