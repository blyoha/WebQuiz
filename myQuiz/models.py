from django.db import models


class Question(models.Model):
    """Represents a model of a question in the service"""

    # Setting the default model manager
    objects = models.Manager()

    text = models.CharField('Text', max_length=100)
    id = models.IntegerField('ID', primary_key=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    """Represents a model of an answer in the service"""

    # Setting the default model manager
    objects = models.Manager()

    text = models.CharField('Текст', max_length=100)
    id = models.IntegerField('ID', primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    is_right = models.BooleanField(default=False)
    is_checked = models.BooleanField(default=False)

    def is_answered_correct(self) -> bool:
        return self.is_checked == self.is_right

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
