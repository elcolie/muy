from django.db import models


class Category(models.Model):
    foo = models.CharField(max_length=10)


class Question(models.Model):
    question_text = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.question_text[:10]


class PetModel(models.Model):
    kind = models.CharField(max_length=100, choices=(('cat', 'Cat'), ('dog', 'Dog')))
