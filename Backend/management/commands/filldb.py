from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from Backend.models import ModelsMachine, ModelsEngine, ModelsTransmission, \
    ModelsDriveAxle, ModelsSteeringBridge, ServiceCompany, Machine, \
    TypeMaintenance, Maintenance, RecoveryMethod, FailureNode, Claims


def create_models_machine():
    ModelsMachine.objects.create(
        name='Дизельный погрузчик VP D15',
        description="Дисковые тормоза в масляной ванне - СТАНДАРТ для всех погрузчиков VP. Их ресурс более 7 000 "
                    "моточасов. У обычных барабанных максимум 1 000. И никаких промежуточных регулировок."
    )
    ModelsMachine.objects.create(
        name='Газобензиновый погрузчик VP G15',
        description="Зачастую газовое оборудование на бензиновые погрузчики устанавливают небольшие мастерские с "
                    "использованием дешевых компонентов. Двигатели NISSAN поступают к нам на конвейер с "
                    "премиум-оборудованием IMPCO, установленным в Японии в заводских условиях.."
    )
    ModelsMachine.objects.create(
        name='Электропогрузчик VP E15',
        description="При повороте два электромотора вращают колеса электропогрузчика VP серии Е навстречу "
                    "друг другу. По сравнению с обычными погрузчиками с одним двигателем, они разворачиваются "
                    "буквально на пятачке."
    )
    print('Созданы записи в БД: модели машин')


def create_models_engine():
    ModelsEngine.objects.create(
        name='Двигатель 1',
        description='Описание двигателя 1'
    )
    ModelsEngine.objects.create(
        name='Двигатель 2',
        description='Описание двигателя 2'
    )
    ModelsEngine.objects.create(
        name='Двигатель 3',
        description='Описание двигателя 3'
    )
    print('Созданы записи в БД: модели двигателей')


def create_models_transmission():
    ModelsTransmission.objects.create(
        name='Трансмиссия 1',
        description='Описание трансмиссии 1'
    )
    ModelsTransmission.objects.create(
        name='Трансмиссия 2',
        description='Описание трансмиссии 2'
    )
    ModelsTransmission.objects.create(
        name='Трансмиссия 3',
        description='Описание трансмиссии 3'
    )
    print('Созданы записи в БД: модели трансмиссии')


def create_models_drive_axle():
    ModelsDriveAxle.objects.create(
        name='Ведущий мост 1',
        description='Описание ведущего моста 1'
    )
    ModelsDriveAxle.objects.create(
        name='Ведущий мост 2',
        description='Описание ведущего моста 2'
    )
    ModelsDriveAxle.objects.create(
        name='Ведущий мост 3',
        description='Описание ведущего моста 3'
    )
    print('Созданы записи в БД: модели ведущего моста')


def create_models_steering_bridge():
    ModelsSteeringBridge.objects.create(
        name='Управляемый мост 1',
        description='Описание управляемого моста 1'
    )
    ModelsSteeringBridge.objects.create(
        name='Управляемый мост 2',
        description='Описание управляемого моста 2'
    )
    ModelsSteeringBridge.objects.create(
        name='Управляемый мост 3',
        description='Описание управляемого моста 3'
    )
    print('Созданы записи в БД: модели управляемого моста')


def create_models_service_company():
    ServiceCompany.objects.create(
        name='Сервисная компания 1',
        description='Описание сервисной компании 1'
    )
    ServiceCompany.objects.create(
        name='Сервисная компания 2',
        description='Описание сервисной компании 2'
    )
    ServiceCompany.objects.create(
        name='Сервисная компания 3',
        description='Описание сервисной компании 3'
    )
    print('Созданы записи в БД: модели сервисной компании')


def create_machine():
    User.objects.create(username='user')
    Machine.objects.create(
        factory_number_machine="d76q3r4qwqwd",
        models_machine=ModelsMachine.objects.get(id=1),
        models_engine=ModelsEngine.objects.get(id=1),
        factory_number_engine="fa76qwdha",
        model_transmission=ModelsTransmission.objects.get(id=1),
        factory_number_transmission="awf67euiyfac",
        models_drive_axle=ModelsDriveAxle.objects.get(id=1),
        factory_number_drive_axle="af8792tljfag",
        models_steering_bridge=ModelsSteeringBridge.objects.get(id=1),
        factory_number_steering_bridge="aso8iqkwva",
        supply_contract="Договор поставки №123 от 11.11.2022",
        date_of_shipment="2022-11-11",
        consumer='Иванов Иван Иваныч',
        delivery_address='На деревню бабушке',
        equipment='Полный фарш',
        client=User.objects.get(id=1),
        service_company=ServiceCompany.objects.get(id=1)
    )
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
        lst_func = [create_models_machine, create_models_engine, create_models_transmission,
                    create_models_drive_axle, create_models_steering_bridge, create_models_service_company,
                    # create_machine,
                    create_type_mainrenance,
                    create_maintenance,
                    create_recovery_method,
                    create_failure_node,
                    create_claims]
        for func in lst_func:
            try:
                func()
                self.stdout.write(self.style.SUCCESS('Success'))
            except BaseException as e:
                self.stdout.write(self.style.ERROR(f'Error: {e}'))
