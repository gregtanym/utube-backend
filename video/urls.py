from django.urls import path, include, re_path

from video.views import VideoView

urlpatterns = [
    path('list', VideoView.List.as_view()),
    path('upload', VideoView.Upload.as_view()),

]