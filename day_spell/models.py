from django.db import models


class DaySpell(models.Model):
    keyword = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    incantation = models.TextField()
    ingredients = models.TextField(blank=True)
    moon_phase = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.keyword})"

