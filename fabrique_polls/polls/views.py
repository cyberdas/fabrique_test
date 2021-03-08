from rest_framework.decorators import api_view
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, 
                                   HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND)
from rest_framework import viewsets, permissions, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.db.models import Q, Exists
from django.utils import timezone

from .models import (Poll, Question, Choice, 
                     TextAnswer, ChoiceAnswer, MultiChoiceAnswer)
from .mixins import PermissionMixin
from .permissions import IsAdminUserOrReadOnly
from .serializers import (PollsSerializer, QuestionsSerializer, ChoicesSerializer, FinishedPollSerializer,
                          TextAnswerSerializer, ChoiceAnswerSerializer, MultiChoiceAnswerSerializer)
from .utils import get_answers, get_voted_polls


class ActiveViewSet(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
    
    serializer_class = PollsSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    
    def get_queryset(self):
        date = timezone.now()
        return Poll.objects.filter(end_date__gt=date)


class PollsViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAdminUser]
    serializer_class = PollsSerializer

    def get_queryset(self):
        return Poll.objects.all()


class QuestionsViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuestionsSerializer
 
    def get_queryset(self):
        queryset = Question.objects.filter(poll_id=self.kwargs.get("poll_id"))
        return queryset


class ChoicesViewSet(viewsets.ModelViewSet):

    serializer_class = [permissions.IsAdminUser] 
    serializer_class = ChoicesSerializer

    def get_queryset(self):
        queryset = Choice.objects.filter(question_id=self.kwargs.get("question_id"))
        return queryset


@api_view(["POST"])
def text_answer(request):
    serializer = TextAnswerSerializer
    return get_answers(request, serializer)


@api_view(["POST"])
def choice_answer(request):
    serializer = ChoiceAnswerSerializer
    return get_answers(request, serializer)


@api_view(["POST"])
def multi_choice_answer(request):
    serializer = MultiChoiceAnswerSerializer
    return get_answers(request, serializer)


@api_view(["POST"])
def get_finished_polls(request):
    user_id =  request.POST.get("user_id", None)
    if not user_id:
        raise ValidationError({"Ошибка": "Передайте user_id"})
    voted_polls = get_voted_polls(request)  # будет возвращать queryset
    if voted_polls.exists():
        serializer = FinishedPollSerializer(voted_polls, many=True, context={"user_id": user_id})
        return Response(serializer.data, status=HTTP_200_OK)
    raise ValidationError({"Ошибка": "Вы еще не прошли полностью ни один опрос"})
