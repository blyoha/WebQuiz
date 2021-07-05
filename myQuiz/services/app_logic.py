from ..models import Question, Answer


def calculate_results() -> int:
    all_answers = list()
    for q in Question.objects.all():
        all_answers.append(int(all([a.is_answered_correct() for a in q.answer_set.all()])))

    percent = len([a for a in all_answers if a]) / len(all_answers) * 100

    return int(percent)


def clear_db() -> None:
    for obj in Question.objects.all():
        for ans in obj.answer_set.all():
            ans.is_checked = False
            ans.save()


def trace_answer(request, question) -> None:
    checked_ans = list()
    for a in request.POST.getlist('ans'):
        checked_ans.append(question.answer_set.get(pk=a))

    for a in checked_ans:
        a.is_checked = True
        a.save()
