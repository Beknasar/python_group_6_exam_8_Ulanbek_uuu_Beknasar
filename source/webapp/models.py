from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = [
    (DEFAULT_CATEGORY, 'Разное'),
    ('food', "Еда"),
    ('toys', 'Игрушки'),
    ('tech', 'Бытовая техника'),
    ('tools', 'Инструменты'),
    ('chemicals', 'Бытовая химия')
]


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


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews', null=True, verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', related_name='product_reviews', on_delete=models.CASCADE,
                                verbose_name='Продукты')
    text = models.TextField(max_length=2000,  verbose_name='Текст отзыва')
    rating = models.FloatField(verbose_name='Оценка', validators=(MinValueValidator(1),MaxValueValidator(5), ))
    status = models.ForeignKey('webapp.Status', related_name='status', on_delete=models.PROTECT, verbose_name='Статус')

    def __str__(self):
        return f'{self.text} -- {self.author}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural='Отзывы'



class Status(models.Model):
    name = models.CharField(default='Не модерирован', max_length=20, null=False, blank=False, verbose_name='Название статуса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Статус'
        verbose_name_plural='Статусы'