from django.urls import path

from admission import views

urlpatterns = [
    path('candidate/new', views.CandidateCreate.as_view(), name='candidate_new'),
    path('candidate', views.CandidateList.as_view(), name='candidate_list'),
    path('exam/new', views.ExamCreate.as_view(), name='exam_new'),
    path('candidate/<int:pk>', views.CandidateUpdate.as_view(), name='candidate_edit'),
    path('jedi', views.JediList.as_view(), name='jedi_list'),
    path('exam', views.ExamList.as_view(), name='exam_list')
]