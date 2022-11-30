from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user(sender, instance, created, **kwargs):
    role_group = {'CL': 'Client', 'SC': 'Service company', 'MN': 'Manager'}
    if created:
        group = Group.objects.get(name=role_group.get(instance.role))
        instance.groups.add(group)


class User(AbstractUser):
    CHOICES = (
        ('CL', 'Client'),
        ('SC', 'Service company'),
        ('MN', 'Manager')
    )
    role = models.CharField(max_length=2, choices=CHOICES, default='CL', verbose_name='Роль')
    name = models.CharField(max_length=128, null=True, blank=True,
                            help_text='Название (только для Клиента и Сервисной компании)',
                            verbose_name='Название')
    description = models.CharField(max_length=512,
                                   null=True, blank=True,
                                   help_text='Описание (только для Клиента и Сервисной компании)',
                                   verbose_name='Описание')

    def __str__(self):
        return f'{self.name} - {self.get_role_display()}'


class ModelsMachine(models.Model):
    """
    Модель техники
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модели техники'

    def __str__(self):
        return self.name


class ModelsEngine(models.Model):
    """
    Модель двигателя
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Модели двигателя'

    def __str__(self):
        return self.name


class ModelsTransmission(models.Model):
    """
    Модель трансмиссии
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модели трансмиссии'

    def __str__(self):
        return self.name


class ModelsDriveAxle(models.Model):
    """
    Модель ведущего моста
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Модели ведущего моста'

    def __str__(self):
        return self.name


class ModelsSteeringBridge(models.Model):
    """
    Модель управляемого моста
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модели управляемого моста'

    def __str__(self):
        return self.name


class ServiceCompany(models.Model):
    """
    Модель сервисная компания
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Модель сервисная компания'
        verbose_name_plural = 'Модели сервисной компании'

    def __str__(self):
        return self.name


class Machine(models.Model):
    """
    Сущность Машина
    """
    factory_number_machine = models.CharField(max_length=128, unique=True, verbose_name='Заводской номер машины')  # Зав. № машины
    models_machine = models.ForeignKey('ModelsMachine', on_delete=models.DO_NOTHING, verbose_name='Модель техники')  # Модель техники
    models_engine = models.ForeignKey('ModelsEngine', on_delete=models.DO_NOTHING, verbose_name='Модель двигателя')  # Модель двигателя
    factory_number_engine = models.CharField(max_length=128, verbose_name='Зав. № двигателя')  # Зав. № двигателя
    model_transmission = models.ForeignKey('ModelsTransmission', on_delete=models.DO_NOTHING, verbose_name='Модель трансмиссии')  # Модель трансмиссии
    factory_number_transmission = models.CharField(max_length=128, verbose_name='Зав. № трансмиссии')  # Зав. № трансмиссии
    models_drive_axle = models.ForeignKey('ModelsDriveAxle', on_delete=models.DO_NOTHING, verbose_name='Модель ведущего моста')  # Модель ведущего моста
    factory_number_drive_axle = models.CharField(max_length=128, verbose_name='Зав. № ведущего моста')  # Зав. № ведущего моста
    models_steering_bridge = models.ForeignKey('ModelsSteeringBridge',
                                               on_delete=models.DO_NOTHING, verbose_name='Модель управляемого моста')  # Модель управляемого моста
    factory_number_steering_bridge = models.CharField(max_length=128, verbose_name='Зав. № управляемого моста')  # Зав. № управляемого моста
    supply_contract = models.CharField(max_length=128, verbose_name='Договор поставки №, дата')  # Договор поставки №, дата
    date_of_shipment = models.DateField(verbose_name='Дата отгрузки с завода')  # Дата отгрузки с завода
    consumer = models.CharField(max_length=128, verbose_name='Грузополучатель (конечный потребитель)')  # Грузополучатель (конечный потребитель)
    delivery_address = models.CharField(max_length=128, verbose_name='Адрес поставки (эксплуатации)')  # Адрес поставки (эксплуатации)
    equipment = models.CharField(max_length=512, verbose_name='Комплектация (доп. опции)')  # Комплектация (доп. опции)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='client', on_delete=models.DO_NOTHING, verbose_name='Клиент')  # Клиент
    service_company = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='service_company', on_delete=models.DO_NOTHING, verbose_name='Сервисная компания')  # Сервисная компания

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ('date_of_shipment',)

    def __str__(self):
        return self.models_machine.name


class TypeMaintenance(models.Model):
    """
    Вид ТО
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Вид ТО'
        verbose_name_plural = 'Виды ТО'

    def __str__(self):
        return self.name


class Maintenance(models.Model):
    """
    Техническое обслуживание
    """
    machine = models.ForeignKey('Machine', on_delete=models.DO_NOTHING, verbose_name='Модель техники')
    type_maintenance = models.ForeignKey('TypeMaintenance', on_delete=models.DO_NOTHING, verbose_name='Вид ТО')  # Вид ТО
    date_maintenance = models.DateField(verbose_name='Дата проведения ТО')  # Дата проведения ТО
    operating_time = models.PositiveIntegerField(verbose_name='Наработка, м/час')  # Наработка, м/час
    work_order = models.CharField(max_length=128, verbose_name='Заказ-наряд')  # заказ-наряд
    date_work_order = models.DateField(verbose_name='дата заказ-наряда')  # дата заказ-наряда
    service_company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='Сервисная компания')  # Сервисная компания

    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'Технические обслуживания'
        ordering = ('date_maintenance',)

    def __str__(self):
        return f'{self.machine.models_machine} - {self.type_maintenance}'


class RecoveryMethod(models.Model):
    """
    Способ восстановления
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способы восстановления'

    def __str__(self):
        return self.name


class FailureNode(models.Model):
    """
    Узел отказа
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Узел отказа'
        verbose_name_plural = 'Узлы отказа'

    def __str__(self):
        return self.name


class Claims(models.Model):
    """
    Рекламации
    """
    machine = models.ForeignKey('Machine', on_delete=models.DO_NOTHING, verbose_name='Модель техники')
    date_of_rejection = models.DateField(verbose_name='Дата отказа')  # Дата отказа
    operating_time = models.PositiveIntegerField(verbose_name='Наработка, м/час')  # Наработка, м/час
    failure_node = models.ForeignKey('FailureNode', on_delete=models.DO_NOTHING, verbose_name='Узел отказа')  # Узел отказа
    description_failure = models.CharField(max_length=128,  verbose_name='Описание отказа')  # Описание отказа
    recovery_method = models.ForeignKey('RecoveryMethod', on_delete=models.DO_NOTHING, verbose_name='Способ восстановления')  # Способ восстановления
    used_spare_parts = models.CharField(max_length=512, verbose_name='Используемые запасные части')  # Используемые запасные части
    date_recovery = models.DateField(verbose_name='Дата восстановления')  # Дата восстановления
    machine_downtime = models.PositiveIntegerField(null=True, verbose_name='Время простоя техники')  # Время простоя техники

    class Meta:
        verbose_name = 'Рекламации'
        verbose_name_plural = 'Рекламации'
        ordering = ('date_of_rejection',)

    def __str__(self):
        return f'{self.machine.models_machine} - {self.failure_node}'

    # def save(self, instance, *args, **kwargs):
    #     """
    #     Производим подсчет времени простоя
    #     """
    #     super().save(instance, *args, **kwargs)
