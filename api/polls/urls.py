from django.urls import path

from polls.views import PollsListAPIView, AnswerCreateAPIView


urlpatterns = [
    path('active-polls', PollsListAPIView.as_view()),
    path('answers', AnswerCreateAPIView.as_view()),
]
