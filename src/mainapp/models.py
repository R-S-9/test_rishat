from django.db import models


class Item(models.Model):
    """Товар"""
    name = models.CharField(
        max_length=150,
        verbose_name='Товар',
        help_text='Название товара',
    )
    description = models.TextField(
        max_length=3000,
        verbose_name='Описание',
        help_text='Описание товара',
        default=''
    )
    price_rub = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена в рублях',
        help_text='Пример: 1234,99',
    )
    price_usd = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена в долларах',
        help_text='Пример: 1234,99',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
