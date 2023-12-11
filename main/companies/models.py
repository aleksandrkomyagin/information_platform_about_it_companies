"""Database settings of the 'Companies' app."""

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User


class Industry(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Отрасль"
        verbose_name_plural = "Отрасли"

    def __str__(self):
        return self.name


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория сервиса"
        verbose_name_plural = "Категории сервисов"


class Service(models.Model):
    category = models.ForeignKey(
        ServiceCategory, on_delete=models.CASCADE, related_name="services"
    )
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField("Название компании", max_length=100)
    description = models.TextField("Описание")
    email = models.EmailField("E-mail адрес")
    address = models.CharField("Адрес", max_length=200)
    logo = models.ImageField("Логотип компании", upload_to="companies/logo/")
    website = models.URLField("Сайт компании")
    services = models.ManyToManyField(
        Service,
        related_name="companies",
        verbose_name="Услуги",
    )
    industries = models.ManyToManyField(
        Industry,
        related_name="companies",
        verbose_name="Отрасли",
    )
    team_size = models.PositiveIntegerField("Численность компании")
    year_founded = models.PositiveIntegerField(
        "Год основания",
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2100),
        ],
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name="Город",
        related_name="companies",
    )

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        ordering = ("id",)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="favorite",
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name="Компания",
        related_name="in_favorite",
    )

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"
        ordering = ("company",)
        constraints = [
            models.UniqueConstraint(fields=["user", "company"], name="unique_favorite")
        ]

    def __str__(self):
        return f"{self.company} {self.user}"


class Phone(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="phones",
    )
    number = models.CharField(max_length=18)

    def __str__(self):
        return self.number
