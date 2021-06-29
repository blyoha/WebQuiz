from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>', views.question, name='question'),
    path('results', views.results, name='results'),
]
