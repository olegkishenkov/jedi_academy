from django.forms import ModelForm

from admission.models import Candidate, Exam


class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'

class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = ['answer']