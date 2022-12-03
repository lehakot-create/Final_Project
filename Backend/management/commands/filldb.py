import csv
import datetime
import os

from django.conf import settings
from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from Backend.models import ModelsMachine, ModelsEngine, ModelsTransmission, \
    ModelsDriveAxle, ModelsSteeringBridge, Machine, \
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
from .models_failure_node import models_failure_node
from .models_recovery_method import models_recovery_method


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
    User = get_user_model()
    for value in models_client:
        User.objects.create_user(
            username=value.get('username'),
            password=value.get('password'),
            name=value.get('name'),
            role='CL'
        )
    print('Созданы записи в БД: модели клиентов')


def create_models_service_company():
    User = get_user_model()
    for value in models_service_company:
        User.objects.create_user(
            username=value.get('username'),
            password=value.get('password'),
            name=value.get('name'),
            description=value.get('description'),
            role='SC'
        )
    print('Созданы записи в БД: модели сервисной компании')


def create_machine():
    User = get_user_model()
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
            client=User.objects.get(name=value.get('client')),
            consumer=value.get('consumer'),
            delivery_address=value.get('delivery_address'),
            equipment=value.get('equipment'),
            service_company=User.objects.get(name=value.get('service_company'))
        )
    print('Созданы записи в БД: запись о конкретной машине')


def create_type_maintenance():
    for value in models_type_maintenance:
        TypeMaintenance.objects.create(
            name=value.get('name'),
            description=value.get('description')
        )
    print('Созданы записи в БД: модели ТО')


def create_maintenance():
    User = get_user_model()
    path = os.path.join(settings.BASE_DIR, 'Backend/management/commands')

    with open(os.path.join(path, 'maintenance_data.csv'), newline='', encoding='utf-8-sig') as csvfile:
        data = csv.DictReader(csvfile)
        for el in data:
            Maintenance.objects.create(
                machine=Machine.objects.get(factory_number_machine=el.get('factory_number_machine')),
                type_maintenance=TypeMaintenance.objects.get(name=el.get('type_maintenance')),
                date_maintenance=datetime.datetime.strptime(el.get('date_maintenance'), '%m-%d-%y').date(),
                operating_time=el.get('operating_time'),
                work_order=el.get('work_order'),
                date_work_order=datetime.datetime.strptime(el.get('date_work_order'), '%m-%d-%y').date(),
                service_company=User.objects.get(name=el.get('service_company'))
            )
    print('Созданы записи в БД: техническое обслуживание')


def create_recovery_method():
    for value in models_recovery_method:
        RecoveryMethod.objects.create(
            name=value.get('name'),
            description=value.get('description')
        )
    print('Созданы записи в БД: модели способа восстановления')


def create_failure_node():
    for value in models_failure_node:
        FailureNode.objects.create(
            name=value.get('name'),
            description=value.get('description')
        )
    print('Созданы записи в БД: модели узла отказа')


def create_claims():
    User = get_user_model()
    path = os.path.join(settings.BASE_DIR, 'Backend/management/commands')

    with open(os.path.join(path, 'claims_data.csv'), newline='', encoding='utf-8-sig') as csvfile:
        data = csv.DictReader(csvfile)
        for el in data:
            Claims.objects.create(
                machine=Machine.objects.get(factory_number_machine=el.get('factory_number_machine')),
                date_of_rejection=datetime.datetime.strptime(el.get('date_of_rejection'), "%d.%m.%Y").date(),
                operating_time=el.get('operating_time'),
                failure_node=FailureNode.objects.get(name=el.get('failure_node')),
                description_failure=el.get('description_failure'),
                recovery_method=RecoveryMethod.objects.get(name=el.get('recovery_method')),
                used_spare_parts=el.get('used_spare_parts'),
                date_recovery=datetime.datetime.strptime(el.get('date_recovery'), "%d.%m.%Y").date(),
                machine_downtime=el.get('machine_downtime'),
            )
    print('Созданы записи в БД: модели рекламаций')


def create_group_client():
    group = Group.objects.create(name='Client')
    my_permission = Permission.objects.get(codename='view_machine')
    group.permissions.add(my_permission)
    my_permission = Permission.objects.get(codename='view_maintenance')
    group.permissions.add(my_permission)
    my_permission = Permission.objects.get(codename='add_maintenance')
    group.permissions.add(my_permission)
    my_permission = Permission.objects.get(codename='view_claims')
    group.permissions.add(my_permission)


def create_group_service_company():
    group = Group.objects.create(name='Service company')
    my_permission = Permission.objects.get(codename='view_machine')
    group.permissions.add(my_permission)
    my_permission = Permission.objects.get(codename='view_maintenance')
    group.permissions.add(my_permission)
    my_permission = Permission.objects.get(codename='add_maintenance')
    group.permissions.add(my_permission)
    my_permission = Permission.objects.get(codename='view_claims')
    group.permissions.add(my_permission)
    my_permission = Permission.objects.get(codename='add_claims')
    group.permissions.add(my_permission)


def create_group_manager():
    group = Group.objects.create(name='Manager')
    permission_list = ('view_machine', 'add_machine',
                       'view_maintenance', 'add_maintenance',
                       'view_claims','add_claims',
                       'change_modelsmachine', 'add_modelsmachine',
                       'change_modelsengine', 'add_modelsengine',
                       'change_modelstransmission', 'add_modelstransmission',
                       'change_modelsdriveaxle', 'add_modelsdriveaxle',
                       'change_modelssteeringbridge', 'add_modelssteeringbridge',
                       'change_typemaintenance', 'add_typemaintenance',
                       'change_recoverymethod', 'add_recoverymethod',
                       'change_failurenode', 'add_failurenode',
                  )
    for permission in permission_list:
        my_permission = Permission.objects.get(codename=permission)
        group.permissions.add(my_permission)


def create_models_manager():
    User = get_user_model()
    User.objects.create_user(
        username='manager',
        password='123',
        name='Менеджер высшего звена',
        role='MN'
    )
    print('Созданы записи в БД: модели менеджера')


class Command(BaseCommand):
    help = 'Заполняем БД'

    def handle(self, *args, **options):
        lst_func = [
            create_models_machine,
            create_models_engine,
            create_models_transmission,
            create_models_drive_axle,
            create_models_steering_bridge,
            create_group_client,
            create_group_service_company,
            create_group_manager,
            create_models_client,
            create_models_service_company,
            create_machine,
            create_type_maintenance,
            create_maintenance,
            create_recovery_method,
            create_failure_node,
            create_claims,
            create_models_manager,
        ]
        for func in lst_func:
            try:
                func()
                self.stdout.write(self.style.SUCCESS('Success'))
            except BaseException as e:
                self.stdout.write(self.style.ERROR(f'Error: {e}'))
