from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, PollViewSet


# urlpatterns = [
#     path("polls/", polls_list, name="polls_list"),
#     path("polls/<int:pk>/", polls_detail, name="polls_detail"),
# ]

# urlpatterns = [
#     path("polls/", PollList.as_view(), name = "pols_list"),
#     path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
#     path("choices/", ChoiceList.as_view(), name='choice_list'),
#     path("vot/", CreateVote.as_view(), name = "create_vote")
# ]
router = DefaultRouter()
router.register('polls', PollViewSet, basename = 'polls')

urlpatterns = [
    path("polls/", PollList.as_view(), name = "pols_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name = "choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name = "create_vote")
]

urlpatterns += router.urls