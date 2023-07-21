from django.db import models
from django.contrib.auth.models import User

hands_variants = [
    ("1H", "One Hand"),
    ("2H", "Two hands"),
    ("Db", "Double"),
]
bottom_up = [

    (False, "Standard"),
    (True, "Bottom up")]
type = [
    ("B", "Balistics"),
    ("G", "Grind")
]


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    allow_bottom_up = models.BooleanField()
    allow_one_hand = models.BooleanField()
    allow_two_hands = models.BooleanField()
    allow_double = models.BooleanField()
    type = models.CharField(max_length=1, choices=type)

    def __str__(self):
        return self.name


class Session(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    rep_count = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    bottom_up = models.BooleanField(choices=bottom_up, default=False)
    hand = models.CharField(max_length=2, choices=hands_variants, default=hands_variants[0][0])
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default="")

    def __str__(self):
        return f"{self.exercise.name} {self.rep_count} reps with {self.weight} kg"
