from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('myQuiz.urls')),
    # path('quiz/', include('quiz.urls')),
    path('admin/', admin.site.urls),
]
