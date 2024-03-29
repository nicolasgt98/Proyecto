# Generated by Django 5.0.2 on 2024-03-18 17:38

import datetime
import django.db.models.deletion
import recordatorios.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordatorios', '0009_alter_evento_fecha_alter_evento_recordatorio_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.DateField(default=datetime.date(2024, 3, 19), validators=[recordatorios.models.fecha_limite_mayor_que_hoy]),
        ),
        migrations.AlterField(
            model_name='evento',
            name='recordatorio',
            field=models.DateField(default=datetime.date(2024, 3, 19), validators=[recordatorios.models.fecha_recordatorio_mayor_que_hoy]),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fecha_pago',
            field=models.DateField(default=datetime.date(2024, 3, 19), validators=[recordatorios.models.fecha_limite_mayor_que_hoy]),
        ),
        migrations.AlterField(
            model_name='pago',
            name='recordatorio',
            field=models.DateField(default=datetime.date(2024, 3, 19), validators=[recordatorios.models.fecha_recordatorio_mayor_que_hoy]),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fecha_limite',
            field=models.DateField(default=datetime.date(2024, 3, 19), validators=[recordatorios.models.fecha_limite_mayor_que_hoy]),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='recordatorio',
            field=models.DateField(default=datetime.date(2024, 3, 19), validators=[recordatorios.models.fecha_recordatorio_mayor_que_hoy]),
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
