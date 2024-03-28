from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Menu'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Item name')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE,
                             related_name='menu_items')
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               null=True, blank=True)

    class Meta:
        verbose_name = 'Menu_item'

    def __str__(self):
        return self.name
