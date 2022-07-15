# Generated by Django 4.0.5 on 2022-07-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0005_quiz_question_marks_of_user_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('op3', models.CharField(max_length=200, null=True)),
                ('op4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='marks_of_user',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='marks_of_user',
            name='user',
        ),
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Marks_Of_User',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
    ]
