# Generated by Django 5.1.5 on 2025-06-06 21:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paciente', '0001_initial'),
        ('profesional', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reserva', models.DateTimeField()),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Confirmada', 'Confirmada'), ('Cancelada', 'Cancelada')], default='Pendiente', max_length=20)),
                ('paciente', models.ForeignKey(db_column='paciente', on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente')),
                ('profesional', models.ForeignKey(db_column='profesional', on_delete=django.db.models.deletion.CASCADE, to='profesional.profesional')),
            ],
            options={
                'db_table': 'reserva',
            },
        ),
    ]
