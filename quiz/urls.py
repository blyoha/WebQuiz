from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.start_quiz, name='start_quiz'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
