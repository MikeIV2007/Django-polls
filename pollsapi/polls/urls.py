from django.urls import path
from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote

# urlpatterns = [
#     path("polls/", polls_list, name="polls_list"),
#     path("polls/<int:pk>/", polls_detail, name="polls_detail"),
# ]

urlpatterns = [
    path("polls/", PollList.as_view(), name = "pols_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("choices/", ChoiceList.as_view(), name='choice_list'),
    path("vot/", CreateVote.as_view(), name = "create_vote")
]