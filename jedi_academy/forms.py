from django.forms import ModelForm, HiddenInput, TextInput

from admission.models import Candidate, Exam


class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'

class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = ['candidate', 'question', 'answer', 'order_code']
        widgets = {
            'candidate': HiddenInput,
            'question': HiddenInput,
            'order_code': HiddenInput
        }