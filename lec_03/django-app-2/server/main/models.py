from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Quiz(BaseModel):
    """Тест"""
    title = models.CharField(verbose_name='Заголовок', max_length=60)
    info = models.CharField(verbose_name='Информация о тесте', blank=True, max_length=255)
    author = models.CharField(verbose_name='Автор', max_length=30)
    time_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    class Meta:
        verbose_name_plural = 'Тесты'
        verbose_name = 'Тест'
        ordering = ['-title', '-time_update']

    def __str__(self):
        return str(self.title)


class Question(models.Model):
    """Вопрос в тесте"""
    question_info = models.CharField(verbose_name='Содержание вопроса', max_length=255)
    quiz_key = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'
        ordering = ['-question_info']

    def __str__(self):
        return str(self.question_info)


class AnswerOption(models.Model):
    """Вариант ответа на вопрос"""
    option_name = models.CharField(verbose_name='Содержание вопроса', max_length=150)
    is_correct = models.BooleanField(verbose_name='Корректность ответа')
    question_key = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Варианты ответа'
        verbose_name = 'Варинт ответа'

    def __str__(self):
        return f'{self.question_key.question_info}   {self.pk}'
