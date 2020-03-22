from django.db import models

# Create your models here.

class Planet(models.Model):
    name = models.fields.CharField(max_length=255)

class Exam(models.Model):
    questions = models.CharField(max_length=255)

class Jedi(models.Model):
    name = models.fields.CharField(max_length=255)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='jedi')

class Candidate(models.Model):
    name = models.fields.CharField(max_length=255)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='cadnidates')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='candidates')
    exam_answers = models.CharField(max_length=255)
    jedi = models.ForeignKey(Jedi, on_delete=models.CASCADE, related_name='candidates')







