from ..models import Question, Answer


def calculate_results():
    all_answers = list()
    for q in Question.objects.all():
        all_answers.append(int(all([a.is_answered_correct() for a in q.answer_set.all()])))

    # for ans in Answer.objects.all():
    #     all_answers.append(int(ans.is_answered_correct()))

    percent = len([a for a in all_answers if a]) / len(all_answers) * 100

    return int(percent)
