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
        max_length=200, choices=TRANSPORT_CHOICES, verbose_name="Тип транспорта"
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

class Route(models.Model):
    TRANSPORT_CHOICES = [
        ("bus", "Автобусный"),
        ("trolley", "Троллейбусный"),
        ("tram", "Трамвайный"),
    ]

    name = models.CharField(max_length=200, verbose_name="Название маршрута")
    number = models.CharField(max_length=200, verbose_name="Номер маршрута")

    transport_types = models.CharField(
        max_length=200, choices=TRANSPORT_CHOICES, verbose_name="Тип транспорта"
    )

    stops = models.ManyToManyField(
        'Stop',
        symmetrical=False,
        related_name='routes',
        verbose_name="Остановки на маршруте"
    )

    class Meta:
        verbose_name = "Маршрут"
        verbose_name_plural = "Маршруты"
        ordering = ['number']

    def __str__(self):
        return self.name

