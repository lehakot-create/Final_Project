# Generated by Django 4.1.3 on 2022-11-23 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='claims',
            options={'verbose_name': 'Рекламации', 'verbose_name_plural': 'Рекламации'},
        ),
        migrations.AlterModelOptions(
            name='failurenode',
            options={'verbose_name': 'Узел отказа', 'verbose_name_plural': 'Узлы отказа'},
        ),
        migrations.AlterModelOptions(
            name='machine',
            options={'verbose_name': 'Машина', 'verbose_name_plural': 'Машины'},
        ),
        migrations.AlterModelOptions(
            name='maintenance',
            options={'verbose_name': 'Техническое обслуживание', 'verbose_name_plural': 'Технические обслуживания'},
        ),
        migrations.AlterModelOptions(
            name='modelsdriveaxle',
            options={'verbose_name': 'Модель ведущего моста', 'verbose_name_plural': 'Модели ведущего моста'},
        ),
        migrations.AlterModelOptions(
            name='modelsengine',
            options={'verbose_name': 'Модель двигателя', 'verbose_name_plural': 'Модели двигателя'},
        ),
        migrations.AlterModelOptions(
            name='modelsmachine',
            options={'verbose_name': 'Модель техники', 'verbose_name_plural': 'Модели техники'},
        ),
        migrations.AlterModelOptions(
            name='modelssteeringbridge',
            options={'verbose_name': 'Модель управляемого моста', 'verbose_name_plural': 'Модели управляемого моста'},
        ),
        migrations.AlterModelOptions(
            name='modelstransmission',
            options={'verbose_name': 'Модель трансмиссии', 'verbose_name_plural': 'Модели трансмиссии'},
        ),
        migrations.AlterModelOptions(
            name='recoverymethod',
            options={'verbose_name': 'Способ восстановления', 'verbose_name_plural': 'Способы восстановления'},
        ),
        migrations.AlterModelOptions(
            name='servicecompany',
            options={'verbose_name': 'Модель сервисная компания', 'verbose_name_plural': 'Модели сервисной компании'},
        ),
        migrations.AlterModelOptions(
            name='typemaintenance',
            options={'verbose_name': 'Вид ТО', 'verbose_name_plural': 'Виды ТО'},
        ),
        migrations.AlterField(
            model_name='modelsmachine',
            name='description',
            field=models.CharField(max_length=512),
        ),
    ]
