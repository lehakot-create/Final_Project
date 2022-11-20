from django.db import models


class ModelsMachine(models.Model):
    """
    Модель техники
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)


class ModelsEngine(models.Model):
    """
    Модель двигателя
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)


class ModelsTransmission(models.Model):
    """
    Модель трансмиссии
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)


class ModelsDriveAxle(models.Model):
    """
    Модель ведущего моста
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)


class ModelsSteeringBridge(models.Model):
    """
    Модель управляемого моста
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)


class Machine(models.Model):
    """
    Сущность Машина
    """
    factory_number_machine = models.CharField(max_length=128, unique=True)  # Зав. № машины
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
    equipment = models.CharField(max_length=128)  # Комплектация (доп. опции)
    # client = models.ForeignKey('', on_delete=models.DO_NOTHING)  # Клиент
    # service_company = models.ForeignKey('', on_delete=models.DO_NOTHING)  # Сервисная компания
