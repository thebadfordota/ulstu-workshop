from django.shortcuts import render, redirect
from .forms import TestForm
from .services import QuizResultService

quiz = QuizResultService()


def view_home_page(request):
    """Выводит данные на главную страницу и сбрасывает все предыдущие ответы пользователя в списке "answers_dicts"."""
    quiz.clear_answers()
    context = {
        'info': "Нажмите на кнопку, чтобы начать тестирование!",
        'title': "Главная страница",
        'heading': "Добро пожаловать",
        'url_name': "main:test1"
    }
    return render(request, 'main/index.html', context)


def view_test1(request):
    """Выводит данные на страницу с тестом №1. Сохраняет ответы пользователя."""
    quiz_id = 0  # индекс вопроса
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            quiz.get_answers(quiz_id, form)
            print(quiz.user_answers)
            return redirect('main:test2')
    else:
        form = quiz.restore_answers(quiz_id)
    context = quiz.get_context_data(form, quiz_id, 'main:home',
                                    'Вернуться на главную страницу',
                                    'Перейти к следующему вопросу')
    return render(request, 'main/test.html', context)


def view_test2(request):
    """Выводит данные на страницу с тестом №2. Сохраняет ответы пользователя."""
    quiz_id = 1
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            quiz.get_answers(quiz_id, form)
            print(quiz.user_answers)
            return redirect('main:test3')
    else:
        form = quiz.restore_answers(quiz_id)
    context = quiz.get_context_data(form, quiz_id, 'main:test1',
                                    'Вернуться к предыдущему вопросу',
                                    'Перейти к следующему вопросу')
    return render(request, 'main/test.html', context)


def view_test3(request):
    """Выводит данные на страницу с тестом №3. Сохраняет ответы пользователя."""
    quiz_id = 2
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            quiz.get_answers(quiz_id, form)
            print(quiz.user_answers)
            return redirect('main:final')
    else:
        form = quiz.restore_answers(quiz_id)
    context = quiz.get_context_data(form, quiz_id, 'main:test2',
                                    'Вернуться к предыдущему вопросу',
                                    'Перейти к следующему вопросу')
    return render(request, 'main/test.html', context)


def view_final_page(request):
    result = quiz.get_result()
    context = {
        'info': f"Вы прошли тест! Ваш результат: {result}",
        'title': "Конец теста",
        'heading': "Тест пройден",
        'url_name': "main:home"
    }
    return render(request, 'main/index.html', context)