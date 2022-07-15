# Generated by Django 4.0.5 on 2022-07-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
