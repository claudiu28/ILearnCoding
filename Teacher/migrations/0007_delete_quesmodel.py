# Generated by Django 4.0.5 on 2022-07-14 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0006_quesmodel_remove_marks_of_user_quiz_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuesModel',
        ),
    ]
