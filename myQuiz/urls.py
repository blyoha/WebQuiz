from django.urls import path

from . import views

app_name = 'myQuiz'
urlpatterns = [
    path('', views.index),
    path('<int:question_id>', views.question, name='question'),
    path('results', views.results, name='results'),
]
