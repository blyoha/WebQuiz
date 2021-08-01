from ..models import Question


def calculate_results() -> int:
    """Returns a percent of the right answers"""
    all_answers: list = []
    for question in Question.objects.all():
        question_accuracy: int = all([a.is_answered_correct() for a in question.answer_set.all()])
        all_answers.append(question_accuracy)

    percent: float = len([a for a in all_answers if a]) / len(all_answers) * 100

    return int(percent)


def clear_db() -> None:
    """Clears SQL database"""
    for obj in Question.objects.all():
        for ans in obj.answer_set.all():
            ans.is_checked = False
            ans.save()


def trace_answer(request, question) -> None:
    """Registers checked answers"""
    checked_ans: list = []
    for ans in request.POST.getlist('ans'):
        checked_ans.append(question.answer_set.get(pk=ans))

    for ans in checked_ans:
        ans.is_checked = True
        ans.save()
