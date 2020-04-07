from random import randrange
from secrets import randbelow

from django.forms import TextInput, HiddenInput
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from admission.models import Exam, Candidate, Jedi, Question, Planet
from jedi_academy.forms import ExamForm


class CandidateList(ListView):
    model = Candidate

    def get_queryset(self):
        new_queryset = Candidate.objects.filter(planet=self.kwargs['planet_pk'])
        return new_queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['planet'] = Planet.objects.get(pk=self.kwargs['planet_pk'])
        return context


class CandidateCreate(CreateView):
    model = Candidate
    fields = ['name', 'planet', 'photo']
    success_url = reverse_lazy('exam_new', args=[3])

    def post(self, request, *args, **kwargs):
        self.success_url = reverse_lazy('exam_new', args=[3])
        value = super().post(self, request, *args, **kwargs)
        return value

    def form_valid(self, form):
        self.object = form.save()
        self.success_url = reverse_lazy('exam_new', args=[self.object.pk])
        return super().form_valid(form)


class ExamCreate(CreateView):
    model = Exam
    form_class = ExamForm
    success_url = reverse_lazy('exam_new', args=[3])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        candidate = Candidate.objects.get(pk=self.kwargs['candidate_pk'])
        context['form'].fields['candidate'].initial = candidate.pk
        question_pk = randbelow(Question.objects.all().count())+1
        question = Question.objects.get(pk=question_pk)
        context['form'].fields['question'].initial = question.pk
        context['form'].fields['order_code'].initial = '0001'
        context['candidate'] = candidate
        context['question'] = question
        return context

    def post(self, request, *args, **kwargs):
        self.success_url = reverse_lazy('exam_new', args=[kwargs['candidate_pk']])
        value = super().post(self, request, *args, **kwargs)
        return value


class CandidateDetail(DetailView):
    model = Candidate


class ExamList(ListView):
    model = Exam

    def get_queryset(self):
        new_queryset = Exam.objects.filter(candidate=self.kwargs['candidate_pk'])
        return new_queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['candidate'] = Candidate.objects.get(pk=self.kwargs['candidate_pk'])
        return context


class JediList(ListView):
    model = Jedi


class JediDetail(DetailView):
    model = Jedi


class CandidateDetail(DetailView):
    model = Exam


class CandidateUpdate(UpdateView):
    model = Candidate
    fields = ['jedi']
    success_url = reverse_lazy('jedi_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
