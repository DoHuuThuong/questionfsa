# Generated by Django 5.1.1 on 2024-09-09 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0005_question_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='date_created',
        ),
    ]
