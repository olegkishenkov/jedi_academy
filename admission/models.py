import os

from django.db import models

# Create your models here.

class Planet(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Jedi(models.Model):
    name = models.CharField(max_length=255)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='jedi')

    def __str__(self):
        return self.name

def path_and_rename(path):
    def inner(instance, filename):
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            from uuid import uuid4
            filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(path, filename)
    return inner

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='candidates')
    jedi = models.ForeignKey(Jedi, on_delete=models.CASCADE, related_name='candidates', null=True, blank=True)
    photo = models.ImageField(upload_to=path_and_rename('candidates'), null=True, blank=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    phrase = models.CharField(max_length=255)
    candidates = models.ManyToManyField(Candidate, through='Exam')

    def __str__(self):
        return self.phrase

class Exam(models.Model):
    candidate = models.ForeignKey(Candidate, related_name='exams', on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, related_name='exams', on_delete=models.CASCADE, null=True)
    order_code = models.CharField(max_length=4, null=True)
    answer = models.BooleanField(null=True)








