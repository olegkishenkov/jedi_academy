from django.urls import path

from admission import views

urlpatterns = [
    path('candidate/new', views.CandidateCreate.as_view(), name='candidate_new'),
    path('candidate/<int:planet_pk>', views.CandidateList.as_view(), name='candidate_list'),
    path('exam/new/<int:candidate_pk>', views.ExamCreate.as_view(), name='exam_new'),
    path('candidate1/<int:pk>', views.CandidateUpdate.as_view(), name='candidate_edit'),
    path('jedi', views.JediList.as_view(), name='jedi_list'),
    path('exam/<candidate_pk>', views.ExamList.as_view(), name='exam_list')
]