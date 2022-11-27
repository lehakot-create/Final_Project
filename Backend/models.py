from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    CHOICES = (
        ('CL', 'Client'),
        ('SC', 'Service company'),
        ('MN', 'Manager')
    )
    role = models.CharField(max_length=2, choices=CHOICES)
    name = models.CharField(max_length=128, help_text='Название (только для Клиента и Сервисной компании)')
    description = models.CharField(max_length=512, help_text='Описание (только для Клиенита и Сервисной компании)')


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
    models_machine = models.ForeignKey('ModelsMachine', on_delete=models.DO_NOTHING)  # Модель техники
    models_engine = models.ForeignKey('ModelsEngine', on_delete=models.DO_NOTHING)  # Модель двигателя
    factory_number_engine = models.CharField(max_length=128)  # Зав. № двигателя
    model_transmission = models.ForeignKey('ModelsTransmission', on_delete=models.DO_NOTHING)  # Модель трансмиссии
    factory_number_transmission = models.CharField(max_length=128)  # Зав. № трансмиссии
    models_drive_axle = models.ForeignKey('ModelsDriveAxle', on_delete=models.DO_NOTHING)  # Модель ведущего моста
    factory_number_drive_axle = models.CharField(max_length=128)  # Зав. № ведущего моста
    models_steering_bridge = models.ForeignKey('ModelsSteeringBridge',
                                               on_delete=models.DO_NOTHING)  # Модель управляемого моста
    factory_number_steering_bridge = models.CharField(max_length=128)  # Зав. № управляемого моста
    supply_contract = models.CharField(max_length=128)  # Договор поставки №, дата
    date_of_shipment = models.DateField()  # Дата отгрузки с завода
    consumer = models.CharField(max_length=128)  # Грузополучатель (конечный потребитель)
    delivery_address = models.CharField(max_length=128)  # Адрес поставки (эксплуатации)
    equipment = models.CharField(max_length=512)  # Комплектация (доп. опции)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='client', on_delete=models.DO_NOTHING)  # Клиент
    service_company = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='service_company', on_delete=models.DO_NOTHING)  # Сервисная компания

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

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
    machine = models.ForeignKey('Machine', on_delete=models.DO_NOTHING)
    type_maintenance = models.ForeignKey('TypeMaintenance', on_delete=models.DO_NOTHING)  # Вид ТО
    date_maintenance = models.DateField()  # Дата проведения ТО
    operating_time = models.PositiveIntegerField()  # Наработка, м/час
    work_order = models.CharField(max_length=128)  # заказ-наряд
    date_work_order = models.DateField()  # дата заказ-наряда
    service_company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)  # Сервисная компания

    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'Технические обслуживания'

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
    machine = models.ForeignKey('Machine', on_delete=models.DO_NOTHING)
    date_of_rejection = models.DateField()  # Дата отказа
    operating_time = models.PositiveIntegerField()  # Наработка, м/час
    failure_node = models.ForeignKey('FailureNode', on_delete=models.DO_NOTHING)  # Узел отказа
    description_failure = models.CharField(max_length=128)  # Описание отказа
    recovery_method = models.ForeignKey('RecoveryMethod', on_delete=models.DO_NOTHING)  # Способ восстановления
    used_spare_parts = models.CharField(max_length=512)  # Используемые запасные части
    date_recovery = models.DateField()  # Дата восстановления
    machine_downtime = models.PositiveIntegerField(null=True)  # Время простоя техники
    service_company = models.ForeignKey('ServiceCompany', on_delete=models.DO_NOTHING, null=True)  # Сервисная компания

    class Meta:
        verbose_name = 'Рекламации'
        verbose_name_plural = 'Рекламации'

    def __str__(self):
        return f'{self.machine.models_machine} - {self.failure_node}'

    # def save(self, instance, *args, **kwargs):
    #     """
    #     Производим подсчет времени простоя
    #     """
    #     super().save(instance, *args, **kwargs)
