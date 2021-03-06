# Generated by Django 3.0.5 on 2021-03-06 11:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20210306_0502'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='multichoiceanswer',
            name='unique_multu_choice_answer',
        ),
        migrations.AlterField(
            model_name='choiceanswer',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='single_choice', to='polls.Choice', verbose_name='Выбор пользователя'),
        ),
        migrations.AlterField(
            model_name='choiceanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_answer', to='polls.Question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='choiceanswer',
            name='user_id',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='id пользователя'),
        ),
        migrations.AlterField(
            model_name='multichoiceanswer',
            name='user_id',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='id пользователя'),
        ),
        migrations.AlterField(
            model_name='textanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='polls.Question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='textanswer',
            name='user_id',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='id пользователя'),
        ),
        migrations.AddConstraint(
            model_name='multichoiceanswer',
            constraint=models.UniqueConstraint(fields=('user_id', 'choice'), name='unique_multi_choice_answer'),
        ),
    ]