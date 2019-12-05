from django_cognito_jwt import JSONWebTokenAuthentication
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from questions.models import Question
from questions.schema import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CognitoQuestionViewSet(viewsets.ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
