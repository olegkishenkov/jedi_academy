# Generated by Django 3.0.4 on 2020-03-23 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0002_auto_20200324_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='jedi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='admission.Jedi'),
        ),
    ]
