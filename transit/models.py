from django.db import models

class TransportType(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name="Код")
    name = models.CharField(max_length=20, verbose_name="Название")

    class Meta:
        verbose_name = "Тип транспорта"
        verbose_name_plural = "Типы транспорта"

    def __str__(self):
        return self.name

class Stop(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название остановки")
    latitude = models.FloatField(verbose_name="Координаты широты")
    longitude = models.FloatField(verbose_name="Координаты долготы")

    transport_types = models.ManyToManyField(
        TransportType, verbose_name="Тип транспорта"
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
    name = models.CharField(max_length=200, verbose_name="Название маршрута")
    number = models.CharField(max_length=200, verbose_name="Номер маршрута")

    transport_types = models.ForeignKey(
        TransportType, on_delete=models.CASCADE, verbose_name="Тип транспорта"
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


class Schedule(models.Model):
    WEEKDAY_CHOICES = [
        (0, "Понедельник"),
        (1, "Вторник"),
        (2, "Среда"),
        (3, "Четверг"),
        (4, "Пятница"),
        (5, "Суббота"),
        (6, "Воскресенье"),
        (7, "Будние дни"),
        (8, "Выходные дни"),
        (8, "Ежедневно"),
    ]

    stop = models.ForeignKey("Stop", on_delete=models.CASCADE, verbose_name="Остановка")
    route = models.ForeignKey("Route", on_delete=models.CASCADE, verbose_name="Маршрут")
    weekday = models.IntegerField(choices=WEEKDAY_CHOICES, verbose_name="День недели")
    arrival_time = models.TimeField(verbose_name="Время прибытия")

    class Meta:
        verbose_name = "Расписание рейса"
        verbose_name_plural = "Расписания рейсов"
        ordering = ["stop", "route", "weekday", "arrival_time"]

    def __str__(self):
        return self.arrival_time