from rest_framework.generics import CreateAPIView

from polls.models import Answer
from polls.serializers import AnswerSerializer


class AnswerCreateAPIView(CreateAPIView):

    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
