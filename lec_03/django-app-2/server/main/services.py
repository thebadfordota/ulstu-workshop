from .forms import TestForm


class QuizResultService:
    questions_info = [
        {
            'info': 'Эталонным интерпретатором языка программирования Python является: ',
            'title': 'Вопрос №1',
            'question_1': 'IronPython',
            'question_2': 'CPython',
            'question_3': 'PyPy',
            'question_4': 'Jython',
            'right': 'option_2'
        },
        {
            'info': 'Какой интерпретатор языка программирования Python использует технологию JIT-компиляции: ',
            'title': 'Вопрос №2',
            'question_1': "PyPy",
            'question_2': "Jython",
            'question_3': "IronPython",
            'question_4': "CPython",
            'right': 'option_1'
        },
        {
            'info': 'Где правильно создана переменная: ',
            'title': 'Вопрос №3',
            'question_1': "let a = 15",
            'question_2': "a = int(15)",
            'question_3': "int a = 15",
            'question_4': "$a = 15",
            'right': 'option_2'
        }
    ]

    def __init__(self):
        self.user_answers = [
            {"option_1": False, "option_2": False, "option_3": False, "option_4": False},
            {"option_1": False, "option_2": False, "option_3": False, "option_4": False},
            {"option_1": False, "option_2": False, "option_3": False, "option_4": False}
        ]

    def clear_answers(self) -> None:
        """Стирает все ответы из списка 'user_answers'."""
        for i in range(len(self.user_answers)):
            for key, value in self.user_answers[i].items():
                self.user_answers[i][key] = False

    def get_answers(self, quiz_id: int, form: TestForm) -> None:
        """Заполняет список ('user_answers') с ответами пользователя, полученными из формы."""
        for key, value in self.user_answers[quiz_id].items():
            self.user_answers[quiz_id][key] = form.cleaned_data[key]

    def get_context_data(self, form: TestForm, quiz_id: int, url_name: str,
                         return_button='Вернуться', submit_button='Продолжить') -> dict:
        """Формирование словаря 'context' для страницы с вопросами."""
        context = {
            'form': form,
            'info': self.questions_info[quiz_id]['info'],
            'title': self.questions_info[quiz_id]['title'],
            'heading': self.questions_info[quiz_id]['title'],
            'question_1': self.questions_info[quiz_id]['question_1'],
            'question_2': self.questions_info[quiz_id]['question_2'],
            'question_3': self.questions_info[quiz_id]['question_3'],
            'question_4': self.questions_info[quiz_id]['question_4'],
            'url_name': url_name,
            'return_button': return_button,
            'submit_button': submit_button
        }
        return context

    def restore_answers(self, quiz_id: int) -> TestForm:
        """Возвращает форму с предыдущими ответами пользователя."""
        form = TestForm(initial={
            'option_1': self.user_answers[quiz_id]["option_1"],
            'option_2': self.user_answers[quiz_id]["option_2"],
            'option_3': self.user_answers[quiz_id]["option_3"],
            'option_4': self.user_answers[quiz_id]["option_4"]
        })
        return form

    def get_result(self) -> float:
        correct_answers = 0
        for i in range(len(self.user_answers)):
            cnt = 0
            for key, value in self.user_answers[i].items():
                if key == self.questions_info[i]['right']:
                    if value:
                        cnt += 1
                elif key != self.questions_info[i]['right']:
                    if not value:
                        cnt += 1
            if cnt == 4:
                correct_answers += 1

        return correct_answers / len(self.questions_info)
