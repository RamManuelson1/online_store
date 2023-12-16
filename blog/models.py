from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
     """модель блоговой записи"""
     title = models.CharField(max_length=150, verbose_name='заголовок')
     slug = models.CharField(max_length=150, **NULLABLE, verbose_name='slug')
     content = models.TextField(verbose_name='содержимое')
     preview = models.ImageField(**NULLABLE, upload_to='articles/', verbose_name='превью')
     created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
     is_published = models.BooleanField(default=True, verbose_name='признак публикации')
     views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

     def __str__(self):
         return f'{self.title}'

     class Meta:
         verbose_name = 'статья'
         verbose_name_plural = 'статьи'

