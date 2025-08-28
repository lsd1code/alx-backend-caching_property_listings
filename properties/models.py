from django.db import models


class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id} - {self.title}'  # type:ignore
