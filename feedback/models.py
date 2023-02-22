from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(3)])
    surname = models.CharField(max_length=60)
    feedback = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10) ])

    def __str__(self):
        return f'Имя: {self.name},  Фамилия: {self.surname}, Отзыв: {self.feedback}, Оценка: {self.rating}'


# from feedback.models import Feedback
# Feedback.objects.all()
