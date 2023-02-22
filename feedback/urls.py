
from django.urls import path
from .views import index, done, update_feedback, FeedBackView, UpdateFeedBack, DoneView, ListFeedBack, DetailFeedBack
urlpatterns = [
    path('done', DoneView.as_view()),
    path('', FeedBackView.as_view()),
    path('<int:id_feedback>', UpdateFeedBack.as_view()),
    path('list', ListFeedBack.as_view()),
    path('detail/<id_feedback>',DetailFeedBack.as_view()),
]