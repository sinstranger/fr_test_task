from rest_framework.generics import ListAPIView

from polls.models import Poll
from polls.serializers import PollSerializer


class PollsListAPIView(ListAPIView):

    serializer_class = PollSerializer
    queryset = Poll.objects.active_polls()
