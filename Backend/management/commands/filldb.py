import csv
import datetime
import os

from django.conf import settings
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
from .models_type_maintenance import models_type_maintenance


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
    print('Созданы записи в БД: запись о конкретной машине')


def create_type_mainrenance():
    for value in models_type_maintenance:
        TypeMaintenance.objects.create(
            name=value.get('name'),
            description=value.get('description')
        )
    print('Созданы записи в БД: модели ТО')


def create_maintenance():
    path = os.path.join(settings.BASE_DIR, 'Backend/management/commands')

    with open(os.path.join(path, 'data.csv'), newline='', encoding='utf-8-sig') as csvfile:
        data = csv.DictReader(csvfile)
        for el in data:
            print(el)
            print(el.get('factory_number_machine'))
            Maintenance.objects.create(
                machine=Machine.objects.get(factory_number_machine=el.get('factory_number_machine')),
                type_maintenance=TypeMaintenance.objects.get(name=el.get('type_maintenance')),
                date_maintenance=datetime.datetime.strptime(el.get('date_maintenance'), '%m-%d-%y').date(),
                operating_time=el.get('operating_time'),
                work_order=el.get('work_order'),
                date_work_order=datetime.datetime.strptime(el.get('date_work_order'), '%m-%d-%y').date(),
                service_company=ServiceCompany.objects.get(name=el.get('service_company'))
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
            # create_models_machine,
            # create_models_engine,
            # create_models_transmission,
            # create_models_drive_axle,
            # create_models_steering_bridge,
            # create_models_service_company,
            # create_models_client,
            # create_machine,
            #
            # create_type_mainrenance,
            create_maintenance,
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
