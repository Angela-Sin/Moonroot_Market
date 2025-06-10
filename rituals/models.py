from django.db import models


class Ritual(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField(help_text="Step-by-step instructions")
    related_products = models.TextField(
        help_text="List or description of related products"
    )
    image = models.ImageField(
        upload_to='ritual_images/', blank=True, null=True
    )

    def __str__(self):
        return self.name
