from django.db import models


class Menu(models.Model):
    """
    Модель, представляющая элемент меню.

    Поля:
        name (CharField): имя элемента меню.
        parent (ForeignKey): родительский элемент меню.
        title (CharField): заголовок элемента меню.
        url (CharField): адрес страницы, на которую ведет элемент меню.
        named_url (CharField): имя именованного адреса, на который ведет элемент меню.
        is_active (BooleanField): флаг, указывающий, является ли элемент активным на текущей странице.

    Методы:
        __str__(): возвращает строковое представление элемента меню.
    """

    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='Untitled')
    url = models.CharField(max_length=255, blank=True)
    named_url = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        """
        Сортировка
        """
        ordering = ['name', 'parent__id', 'id']

    def __str__(self):
        """
        Возвращает строковое представление элемента меню.
        """
        return self.title or self.name
