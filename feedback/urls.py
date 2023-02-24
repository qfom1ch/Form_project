
from django.urls import path
from .views import FeedBackView, UpdateFeedBack, DoneView, ListFeedBack, DetailFeedBack, FeedBackViewUpdate
urlpatterns = [
    path('done', DoneView.as_view()),
    path('', FeedBackView.as_view()),
    path('<int:id_feedback>', UpdateFeedBack.as_view()),
    path('list', ListFeedBack.as_view()),
    path('detail/<int:pk>',DetailFeedBack.as_view()),
    path('update/<int:pk>',FeedBackViewUpdate.as_view()),
]