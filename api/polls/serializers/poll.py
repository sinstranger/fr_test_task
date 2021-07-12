from rest_framework.serializers import ModelSerializer

from polls.models import Poll, Question


class QuestionSerializer(ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'

class PollSerializer(ModelSerializer):

    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ['name', 'start_date', 'finish_date', 'description', 'questions']
