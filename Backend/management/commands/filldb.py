from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from Backend.models import ModelsMachine, ModelsEngine, ModelsTransmission, \
    ModelsDriveAxle, ModelsSteeringBridge, ServiceCompany, Machine, \
    TypeMaintenance, Maintenance, RecoveryMethod, FailureNode, Claims

from .models_machine import models_machine
from .models_engine import models_engine
from .models_transmission import models_transmission
from .models_drive_axle import models_drive_axle
from .models_steering_bridge import models_steering_bridge
from .models_client import models_client
from .models_service_company import models_service_company
from .machine import machine


def create_models_machine():
    for value in models_machine:
        ModelsMachine.objects.create(
            name=value.get('name'),
            description=value.get('description')
        )
    print('Созданы записи в БД: модели машин')


def create_models_engine():
    for value in models_engine:
        ModelsEngine.objects.create(
            name=value.get('name'),
            description=value.get('description')
        )
    print('Созданы записи в БД: модели двигателей')


def create_models_transmission():
    for value in models_transmission:
        ModelsTransmission.objects.create(
            name=value.get('name'),
            description=value.get('description')
        )
    print('Созданы записи в БД: модели трансмиссии')


def create_models_drive_axle():
    for value in models_drive_axle:
        ModelsDriveAxle.objects.create(
            name=value.get('name'),
            description=value.get('description')
        )
    print('Созданы записи в БД: модели ведущего моста')


def create_models_steering_bridge():
    for value in models_steering_bridge:
        ModelsSteeringBridge.objects.create(
            name=value.get('name'),
            description=value.get('description')
        )
    print('Созданы записи в БД: модели управляемого моста')


def create_models_client():
    for value in models_client:
        User.objects.create(
            username=value.get('username')
        )
    print('Созданы записи в БД: модели клиентов')


def create_models_service_company():
    for value in models_service_company:
        ServiceCompany.objects.create(
            name=value.get('name'),
            description=value.get('description')
        )
    print('Созданы записи в БД: модели сервисной компании')


def create_machine():
    for value in machine:
        Machine.objects.create(
            models_machine=ModelsMachine.objects.get(name=value.get('models_machine')),
            factory_number_machine=value.get('factory_number_machine'),
            models_engine=ModelsEngine.objects.get(name=value.get('models_engine')),
            factory_number_engine=value.get('factory_number_engine'),
            model_transmission=ModelsTransmission.objects.get(name=value.get('model_transmission')),
            factory_number_transmission=value.get('factory_number_transmission'),
            models_drive_axle=ModelsDriveAxle.objects.get(name=value.get('models_drive_axle')),
            factory_number_drive_axle=value.get('factory_number_drive_axle'),
            models_steering_bridge=ModelsSteeringBridge.objects.get(name=value.get('models_steering_bridge')),
            factory_number_steering_bridge=value.get('models_drive_axle'),
            date_of_shipment=value.get('date_of_shipment'),
            client=User.objects.get(username=value.get('client')),
            consumer=value.get('consumer'),
            delivery_address=value.get('delivery_address'),
            equipment=value.get('equipment'),
            service_company=ServiceCompany.objects.get(name=value.get('service_company'))
        )
    # User.objects.create(username='user')
    # Machine.objects.create(
    #     factory_number_machine="d76q3r4qwqwd",
    #     models_machine=ModelsMachine.objects.get(id=1),
    #     models_engine=ModelsEngine.objects.get(id=1),
    #     factory_number_engine="fa76qwdha",
    #     model_transmission=ModelsTransmission.objects.get(id=1),
    #     factory_number_transmission="awf67euiyfac",
    #     models_drive_axle=ModelsDriveAxle.objects.get(id=1),
    #     factory_number_drive_axle="af8792tljfag",
    #     models_steering_bridge=ModelsSteeringBridge.objects.get(id=1),
    #     factory_number_steering_bridge="aso8iqkwva",
    #     supply_contract="Договор поставки №123 от 11.11.2022",
    #     date_of_shipment="2022-11-11",
    #     consumer='Иванов Иван Иваныч',
    #     delivery_address='На деревню бабушке',
    #     equipment='Полный фарш',
    #     client=User.objects.get(id=1),
    #     service_company=ServiceCompany.objects.get(id=1)
    # )
    print('Созданы записи в БД: запись о конкретной машине')


def create_type_mainrenance():
    TypeMaintenance.objects.create(
        name='ТО 1',
        description='Описание ТО 1'
    )
    TypeMaintenance.objects.create(
        name='ТО 2',
        description='Описание ТО 2'
    )
    TypeMaintenance.objects.create(
        name='ТО 3',
        description='Описание ТО 3'
    )
    print('Созданы записи в БД: модели ТО')


def create_maintenance():
    Maintenance.objects.create(
        machine=Machine.objects.get(id=1),
        type_maintenance=TypeMaintenance.objects.get(id=1),
        date_maintenance="2022-11-13",
        operating_time=3000,
        work_order=123,
        date_work_order="2022-11-13",
        service_company=ServiceCompany.objects.get(id=1)
    )
    print('Созданы записи в БД: техническое обслуживание')


def create_recovery_method():
    RecoveryMethod.objects.create(
        name='Способ восстановления 1',
        description='Описание способа восстановления 1'
    )
    RecoveryMethod.objects.create(
        name='Способ восстановления 2',
        description='Описание способа восстановления 2'
    )
    RecoveryMethod.objects.create(
        name='Способ восстановления 3',
        description='Описание способа восстановления 3'
    )
    print('Созданы записи в БД: модели способа восстановления')


def create_failure_node():
    FailureNode.objects.create(
        name='Узел отказа 1',
        description='Описание узла отказа 1'
    )
    FailureNode.objects.create(
        name='Узел отказа 2',
        description='Описание узла отказа 2'
    )
    FailureNode.objects.create(
        name='Узел отказа 3',
        description='Описание узла отказа 3'
    )
    print('Созданы записи в БД: модели узла отказа')


def create_claims():
    Claims.objects.create(
        machine=Machine.objects.get(id=1),
        date_of_rejection="2022-11-14",
        operating_time=3000,
        failure_node=FailureNode.objects.get(id=1),
        description_failure="Перестал взлетать",
        recovery_method=RecoveryMethod.objects.get(id=1),
        used_spare_parts="Лопасти, лыжи и акваланг",
        date_recovery="2022-11-15",
        service_company=ServiceCompany.objects.get(id=1)
    )
    print('Созданы записи в БД: модели рекламаций')


class Command(BaseCommand):
    help = 'Заполняем БД'

    def handle(self, *args, **options):
        lst_func = [
            create_models_machine,
            create_models_engine,
            create_models_transmission,
            create_models_drive_axle,
            create_models_steering_bridge,
            create_models_service_company,
            create_models_client,
            create_machine,
            # create_type_mainrenance,
            # create_maintenance,
            # create_recovery_method,
            # create_failure_node,
            # create_claims
        ]
        for func in lst_func:
            try:
                func()
                self.stdout.write(self.style.SUCCESS('Success'))
            except BaseException as e:
                self.stdout.write(self.style.ERROR(f'Error: {e}'))
