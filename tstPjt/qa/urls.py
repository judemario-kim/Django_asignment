from django.urls import path

from . import views

app_name = 'qa'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/statistic/', views.StatisticView.as_view(), name='statistic'),
    path('<int:pk>/exam_main/', views.Exam_mainView.as_view(), name='exam_main'),
    path('make_exam/', views.make_exam, name='make_exam'),
    path('create_exam/', views.create_exam, name='create_exam'),
    path('<int:exam_id>/make_question/', views.make_question, name='make_question'),
    path('<int:exam_id>/create_question/', views.create_question, name='create_question'),
    path('<int:exam_id>/score/', views.score, name='score'),
]