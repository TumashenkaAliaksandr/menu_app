from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='Untitled')
    url = models.CharField(max_length=255, blank=True)
    named_url = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['name', 'parent__id', 'id']
