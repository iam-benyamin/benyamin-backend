from django.db import models


def path_to_save(instance, filename):
    return f"media/abouts/{filename}"


class About(models.Model):
    text = models.TextField()
    pictuer = models.ImageField(
        upload_to=path_to_save, null=True, blank=True, max_length=100)

    def __str__(self):
        return f'{self.text}'
