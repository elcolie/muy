from rest_framework import viewsets

from questions.models import Question
from questions.schema import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer