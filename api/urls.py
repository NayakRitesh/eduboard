from django.urls import path
from api import views

app_name = ' api'

urlpatterns = [
    path('createquestion/', views.create_question, name='createquestion'),
    path('showquestion/', views.show_question, name='showquestion'),
]
