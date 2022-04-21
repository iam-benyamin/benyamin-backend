from django.db import models


def path_to_save(instance, filename):
    return f"media/works/{filename}"


class Work(models.Model):
    link = models.URLField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    pictuer = models.ImageField(
        upload_to=path_to_save, null=True, blank=True, max_length=100)

    def __str__(self):
        return f'{self.title}'
