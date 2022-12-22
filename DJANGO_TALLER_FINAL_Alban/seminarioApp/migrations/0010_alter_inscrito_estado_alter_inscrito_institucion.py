# Generated by Django 4.1.3 on 2022-12-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminarioApp', '0009_alter_inscrito_institucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscrito',
            name='estado',
            field=models.IntegerField(choices=[[0, 'Reservado'], [1, 'Completada'], [2, 'Anulada'], [3, 'No asisten']], verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='inscrito',
            name='institucion',
            field=models.IntegerField(choices=[[0, 'U Catolica'], [1, 'U de Chile'], [2, 'UFRO'], [3, 'Santo Tomas'], [4, 'U Autonoma'], [5, 'Inacap'], [6, 'AIEP']], verbose_name='Institución'),
        ),
    ]