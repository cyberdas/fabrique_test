from django.utils import timezone
from datetime import timedelta

from ..models import Poll, Question, Choice


def create_poll():
    poll = Poll.objects.create(
            title="Первое название",
            start_date=timezone.now() + timedelta(days=1),
            end_date=timezone.now() + timedelta(days=3),
            description="Описание")
    return poll


def create_questions():
    poll = create_poll()
    Question.objects.create(
        text="Текст", poll=poll, question_type="Text"
    )
    Question.objects.create(
        text="Вопрос с выбором", poll=poll, question_type="Choice"
    )
    Question.objects.create(
        text="Несколько выборов", poll=poll, question_type="Multichoice"
    )


def create_choices():
    questions = create_questions()
    pass