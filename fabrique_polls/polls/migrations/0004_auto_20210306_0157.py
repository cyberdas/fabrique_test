# Generated by Django 3.0.5 on 2021-03-05 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210306_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('Text', 'Ответьте текстом'), ('Choice', 'Выберите один вариант'), ('Multichoice', 'Выберите несколько вариантов')], max_length=11, verbose_name='Тип вопроса'),
        ),
    ]
