from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = {
    (DEFAULT_CATEGORY, 'Разное'),
    ('food', "Еда"),
    ('toys', 'Игрушки'),
    ('tech', 'Бытовая техника'),
    ('tools', 'Инструменты'),
    ('chemicals', 'Бытовая химия')
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
# Автор - внешний ключ к пользователю
# Товар - внешний ключ к товару
# Текст отзыва - обязательное, длинный текст
# Оценка - число от 1 до 5, обязательное
class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews', null=True, verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', related_name='product_reviews', on_delete=models.CASCADE,
                                verbose_name='Продукты')
    text = models.TextField(max_length=2000,  verbose_name='Текст отзыва')
    rating = models.IntegerField(verbose_name='Оценка', validators=(MinValueValidator(0),MaxValueValidator(5), ))

