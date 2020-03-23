from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from admission.models import Exam, Candidate, Jedi


class CandidateList(ListView):
    model = Candidate

class CandidateCreate(CreateView):
    model = Candidate
    fields = ['name', 'planet']
    success_url = reverse_lazy('exam_new')

class ExamCreate(CreateView):
    model = Exam
    fields = ['candidate', 'question', 'answer', 'order_code']
    success_url = reverse_lazy('exam_new')

class CandidateDetail(DetailView):
    model = Candidate

class ExamList(ListView):
    model = Exam

class JediList(ListView):
    model = Jedi

class JediDetail(DetailView):
    model = Jedi

class CandidateDetail(DetailView):
    model = Exam

class CandidateUpdate(UpdateView):
    model = Candidate
    fields = ['name', 'planet', 'jedi']
    success_url = reverse_lazy('jedi_list')