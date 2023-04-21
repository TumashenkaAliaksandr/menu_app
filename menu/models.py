from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    """
    Модель для хранения пунктов меню.
    """
    name = models.CharField(max_length=100, verbose_name='название')
    url = models.CharField(max_length=100, verbose_name='URL')

    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True,
        verbose_name='родительский пункт', related_name='children'
    )

    class Meta:
        verbose_name = 'пункт меню'
        verbose_name_plural = 'пункты меню'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Метод для получения URL текущего пункта меню.
        """
        return reverse(self.url)


class Menu(models.Model):
    """
    Модель для хранения меню.
    """
    name = models.CharField(max_length=100, verbose_name='название')
    items = models.ManyToManyField(MenuItem, verbose_name='пункты меню', blank=True)

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'

    def __str__(self):
        return self.name
