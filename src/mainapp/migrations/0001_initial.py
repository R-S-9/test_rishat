# Generated by Django 4.1.6 on 2023-02-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название товара', max_length=150, verbose_name='Товар')),
                ('description', models.TextField(default='', help_text='Описание товара', max_length=3000, verbose_name='Описание')),
                ('price_rub', models.DecimalField(decimal_places=2, help_text='Пример: 199,99', max_digits=10, verbose_name='Цена в рублях')),
                ('price_rub_cod', models.CharField(max_length=100, verbose_name='Код цены в рублях')),
                ('price_usd', models.DecimalField(decimal_places=2, help_text='Пример: 199,99', max_digits=10, verbose_name='Цена в долларах')),
                ('price_usd_cod', models.CharField(max_length=100, verbose_name='Код цены в долларах')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
