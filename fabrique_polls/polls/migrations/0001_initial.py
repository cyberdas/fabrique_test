# Generated by Django 3.0.5 on 2021-03-05 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название опроса')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('end_date', models.DateTimeField(verbose_name='Дата окончания')),
                ('description', models.TextField(verbose_name='Описание')),
                ('active', models.BooleanField(default=True, verbose_name='активный')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
                ('question_type', models.CharField(choices=[('Text', 'Ответьте текстом'), ('Choice', 'Выберите один вариант'), ('Multichoice', 'Выберите несколько вариантов')], default='Text', max_length=11, verbose_name='Тип вопроса')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='polls.Poll', verbose_name='Опрос')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=64)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_choices', to='polls.Question')),
            ],
            options={
                'verbose_name': 'Вариант ответа',
                'verbose_name_plural': 'Варианты ответов',
            },
        ),
    ]
