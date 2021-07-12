from django.core.exceptions import ObjectDoesNotExist
from rest_framework.serializers import ModelSerializer, ValidationError

from polls.models import Answer, Question


class AnswerSerializer(ModelSerializer):

    ERROR_TEXT_IN_OPTIONS = (
        'В ответе к вопросу с вариантами ответов должны быть только цифры вариантов, разделенные пробелами')
    ERROR_TOO_MANY_OPTIONS = 'Количество вариантов больше, чем указано в вопросе'
    ERROR_UNACCEPTABLE_OPTION = 'Значения вариантов ответов больше, чем максимальное количество вариантов'

    class Meta:
        model = Answer
        fields = '__all__'

    def validate_answer(self, value):
        if self._question.kind == Question.KIND_OPTIONS:
            self._validate_options_answer(value)
            self._validate_options_number(value)
            self._validate_options_values(value)

    def _validate_options_answer(self, value):
        """ Проверяем, что ответ - это строка с цифрами, разделенная пробелами """
        if not all([option.isnumeric() for option in value.split()]):
            raise ValidationError(detail=self.ERROR_TEXT_IN_OPTIONS)

    def _validate_options_number(self, value):
        """ Количество ответов на вопрос с вариантами не больше допустимого в вопросе количества """
        if len(value.split()) > self._question.number_of_answers:
            raise ValidationError(detail=self.ERROR_TOO_MANY_OPTIONS)

    def _validate_options_values(self, value):
        """
        Значения вариантов не должны быть больше количества правильных вариантов.
        Т.е. если допустимо только 3 варианта ответа, то нельзя передавать 4 в качестве варианта
        """
        max_value = self._question.number_of_answers
        for option in [int(option) for option in value.split()]:
            if option > max_value:
                raise ValidationError(detail=self.ERROR_UNACCEPTABLE_OPTION)

    @property
    def _question(self):
        try:
            return Question.objects.get(pk=self.initial_data.get('question'))
        except ObjectDoesNotExist:
            raise ValidationError()
