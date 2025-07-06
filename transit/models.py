from django.db import models

class Stop(models.Model):
    TRANSPORT_CHOICES = [
        ('bus', 'Автобусная'),
        ('trolley', 'Троллейбусная'),
        ('bus-trolley', 'Автобусная-троллейбусная'),
        ('tram', 'Трамвайная'),
    ]

    name = models.CharField(max_length=200, verbose_name="Название остановки")
    latitude = models.FloatField(verbose_name="Координаты широты")
    longitude = models.FloatField(verbose_name="Координаты долготы")

    transport_types = models.CharField(
        max_length=200, choices=TRANSPORT_CHOICES, verbose_name="Тип приходящего транспорта"
    )

    next_stops = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='previous_stops',
        verbose_name='Следующие остановки'
    )

    class Meta:
        verbose_name = "Остановка"
        verbose_name_plural = "Остановки"
        ordering = ['name']

    def __str__(self):
        return self.name