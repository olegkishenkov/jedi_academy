from django.contrib import admin

# Register your models here.
from admission.models import Planet, Exam, Jedi, Candidate, Question

admin.site.register(Planet)
admin.site.register(Exam)
admin.site.register(Jedi)
admin.site.register(Candidate)
admin.site.register(Question)
