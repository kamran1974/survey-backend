from django.db import models


class Feedback(models.Model):
    # 9 questions with 4 choices each (choice fields)
    question_1 = models.CharField(max_length=10,
                                  choices=[('1', 'ضعیف'), ('2', 'متوسط'), ('3', 'خوب'), ('4', 'عالی')])
    question_2 = models.CharField(max_length=10,
                                  choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')])
    question_3 = models.CharField(max_length=10,
                                  choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')])
    question_4 = models.CharField(max_length=10,
                                  choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')])
    question_5 = models.CharField(max_length=10,
                                  choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')])
    question_6 = models.CharField(max_length=10,
                                  choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')])
    question_7 = models.CharField(max_length=10,
                                  choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')])
    question_8 = models.CharField(max_length=10,
                                  choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')])
    question_9 = models.CharField(max_length=10,
                                  choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')])
    question_10 = models.CharField(max_length=10,
                                  choices=[('1', 'ضعیف'), ('2', ' متوسط'), ('3', 'خوب'), ('4', 'عالی')])

    # 10 boolean questions
    boolean_1 = models.BooleanField(default=False)
    boolean_2 = models.BooleanField(default=False)
    boolean_3 = models.BooleanField(default=False)
    boolean_4 = models.BooleanField(default=False)
    boolean_5 = models.BooleanField(default=False)
    boolean_6 = models.BooleanField(default=False)
    boolean_7 = models.BooleanField(default=False)
    boolean_8 = models.BooleanField(default=False)
    boolean_9 = models.BooleanField(default=False)
    boolean_10 = models.BooleanField(default=False)

    # Optional text feedback
    text_feedback = models.TextField(blank=True, null=True)

    # Timestamp for when feedback was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.id} - {self.created_at}"
