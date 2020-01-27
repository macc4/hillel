from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import Question, Choice

from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from polls.serializers import QuestionSerializer, ChoiceSerializer


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = LimitOffsetPagination


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = QuestionSerializer

    def get_object(self):
        obj = get_object_or_404(Question, pk=self.kwargs.get('question_id'))
        return obj


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    pagination_class = LimitOffsetPagination


class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ChoiceSerializer

    def get_object(self):
        obj = get_object_or_404(Choice, pk=self.kwargs.get('choice_id'))
        return obj


def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    return HttpResponse(', '.join([q.question_text for q in question_list]))
