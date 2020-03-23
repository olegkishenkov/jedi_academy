# Generated by Django 3.0.4 on 2020-03-23 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='exam_answers',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='questions',
        ),
        migrations.AddField(
            model_name='exam',
            name='answer',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='admission.Candidate'),
        ),
        migrations.AddField(
            model_name='exam',
            name='order_code',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phrase', models.CharField(max_length=255)),
                ('answer', models.BooleanField()),
                ('candidates', models.ManyToManyField(through='admission.Exam', to='admission.Candidate')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='admission.Question'),
        ),
    ]
