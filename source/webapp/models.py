from django.db import models


DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = {
    (DEFAULT_CATEGORY, 'Разное'),
    ('food', "Еда"),
    ('toys', 'Игрушки'),
    ('tech', 'Бытовая техника'),
    ('tools', 'Инструменты')
}


class Product(models.Model):
    name = models.CharField(max_length=35, null=False, blank=False, verbose_name='Название')
    category = models.CharField(max_length=20, default=DEFAULT_CATEGORY, choices=CATEGORY_CHOICES, verbose_name='Категория')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    picture = models.ImageField(null=True, blank=True, upload_to='product_pics', verbose_name='Картинка продукта')

    def __str__(self):
        return f'{self.name} -- {self.category}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'