# Generated by Django 3.2.4 on 2021-06-29 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='choice_text',
            new_name='answer_text',
        ),
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
    ]
