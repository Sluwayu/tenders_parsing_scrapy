# Generated by Django 4.2 on 2023-04-27 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JuridicalPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Наименование юрлица')),
                ('short_name', models.TextField(null=True, verbose_name='Краткое наименование')),
                ('registration_date', models.DateTimeField(verbose_name='Дата регистрации')),
                ('inn', models.CharField(max_length=20, unique=True, verbose_name='ИНН')),
                ('ogrn', models.CharField(max_length=20, verbose_name='ОГРН')),
                ('kpp', models.CharField(max_length=20, verbose_name='КПП')),
                ('web_site', models.URLField(null=True, verbose_name='Адрес web сайта')),
                ('eis_number', models.CharField(max_length=20, verbose_name='Номер в ЕИС')),
                ('telephone', models.CharField(max_length=20, null=True, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('fax', models.CharField(max_length=20, null=True, verbose_name='Факс')),
                ('contact_person', models.CharField(max_length=100, verbose_name='Контактное лицо')),
                ('address', models.TextField(verbose_name='Юридический адрес')),
            ],
            options={
                'verbose_name': 'Юридическое лицо',
                'verbose_name_plural': 'Юридические лица',
            },
        ),
        migrations.CreateModel(
            name='ObjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Наименование объекта закупки')),
            ],
            options={
                'verbose_name': 'Тип объекта закупки',
                'verbose_name_plural': 'Типы объекта закупки',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Наименование региона')),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
            },
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, unique=True, verbose_name='Номер закупки')),
                ('title', models.TextField(db_index=True, verbose_name='Наименование закупки')),
                ('price', models.FloatField(verbose_name='Сумма закупки (руб.)')),
                ('start_date', models.DateTimeField(verbose_name='Дата начала')),
                ('end_date', models.DateTimeField(verbose_name='Дата окончания')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_tenders', to='web_app.juridicalperson', verbose_name='Заказчик')),
                ('customer_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tenders', to='web_app.region', verbose_name='Регион заказчика')),
                ('object_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tenders', to='web_app.objecttype', verbose_name='Тип объекта закупки')),
                ('organizer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organizer_tenders', to='web_app.juridicalperson', verbose_name='Организатор')),
            ],
            options={
                'verbose_name': 'Тендер',
                'verbose_name_plural': 'Тендеры',
                'ordering': ('-start_date',),
            },
        ),
        migrations.CreateModel(
            name='TenderType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Наименование типа закупки')),
            ],
            options={
                'verbose_name': 'Тип закупки',
                'verbose_name_plural': 'Типы закупки',
            },
        ),
        migrations.CreateModel(
            name='TenderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(verbose_name='Код предмета по ОКПД')),
                ('title', models.TextField(db_index=True, verbose_name='Наименование предмета')),
                ('quantity', models.FloatField(verbose_name='Количество')),
                ('price', models.FloatField(verbose_name='Стоимость')),
                ('tender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='web_app.tender', verbose_name='Тендер предмета')),
            ],
            options={
                'verbose_name': 'Предмет закупки/контакта',
                'verbose_name_plural': 'Предметы закупки/контакта',
            },
        ),
        migrations.AddField(
            model_name='tender',
            name='tender_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tenders', to='web_app.tendertype', verbose_name='Тип закупки'),
        ),
        migrations.AddField(
            model_name='juridicalperson',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='juridical_persons', to='web_app.region', verbose_name='Регион'),
        ),
        migrations.AddConstraint(
            model_name='tenderitem',
            constraint=models.UniqueConstraint(fields=('code', 'title', 'quantity', 'price', 'tender'), name='unique_tender_item'),
        ),
    ]
