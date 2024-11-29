# Generated by Django 5.1.3 on 2024-11-29 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.CharField(choices=[('1', 'ضعیف'), ('2', 'متوسط'), ('3', 'خوب'), ('4', 'عالی')], max_length=10)),
                ('question_2', models.CharField(choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')], max_length=10)),
                ('question_3', models.CharField(choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')], max_length=10)),
                ('question_4', models.CharField(choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')], max_length=10)),
                ('question_5', models.CharField(choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')], max_length=10)),
                ('question_6', models.CharField(choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')], max_length=10)),
                ('question_7', models.CharField(choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')], max_length=10)),
                ('question_8', models.CharField(choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')], max_length=10)),
                ('question_9', models.CharField(choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')], max_length=10)),
                ('question_10', models.CharField(choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')], max_length=10)),
                ('boolean_1', models.BooleanField(default=False)),
                ('boolean_2', models.BooleanField(default=False)),
                ('boolean_3', models.BooleanField(default=False)),
                ('boolean_4', models.BooleanField(default=False)),
                ('boolean_5', models.BooleanField(default=False)),
                ('boolean_6', models.BooleanField(default=False)),
                ('boolean_7', models.BooleanField(default=False)),
                ('boolean_8', models.BooleanField(default=False)),
                ('boolean_9', models.BooleanField(default=False)),
                ('boolean_10', models.BooleanField(default=False)),
                ('text_feedback', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]