from django.db import models

# Create your models here.


class Events(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    published = models.DateTimeField(auto_now_add=True)
    period = models.ForeignKey('Period', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['-published']

    def __str__(self):
        return f'{self.title} - {self.published}'


class Period(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Период'
        verbose_name_plural = 'Периоды'

    def __str__(self):
        return self.name
