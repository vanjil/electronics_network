from django.db import models

class NetworkUnit(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    contact_email = models.EmailField(verbose_name="Контактный email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    building_number = models.CharField(max_length=10, verbose_name="Номер дома")
    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='clients',
        verbose_name="Поставщик"
    )
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Задолженность")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название продукта")
    model = models.CharField(max_length=100, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода на рынок")
    network_unit = models.ForeignKey(
        NetworkUnit,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Звено сети"
    )

    def __str__(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"