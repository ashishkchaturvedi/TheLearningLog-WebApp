# Generated by Django 2.2.5 on 2019-09-21 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Toppping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.Pizza')),
            ],
            options={
                'verbose_name_plural': 'toppings',
            },
        ),
    ]
