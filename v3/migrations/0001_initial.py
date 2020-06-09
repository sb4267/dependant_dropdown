# Generated by Django 2.2.7 on 2020-03-13 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Models_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_id', models.CharField(max_length=30)),
                ('model_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v3.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='V_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('model_n', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v3.Models_name')),
            ],
        ),
        migrations.CreateModel(
            name='Main_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gearbox', models.CharField(max_length=100)),
                ('power_ps', models.CharField(max_length=100)),
                ('kilometer', models.CharField(max_length=100)),
                ('fuel_type', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('brand_name_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='v3.Brand')),
                ('model_n', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='v3.V_type')),
                ('model_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='v3.Models_name')),
            ],
        ),
    ]
