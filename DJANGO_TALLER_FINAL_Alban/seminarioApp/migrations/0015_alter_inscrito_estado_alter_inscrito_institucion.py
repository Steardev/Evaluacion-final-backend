# Generated by Django 4.1.3 on 2022-12-17 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminarioApp', '0014_alter_inscrito_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscrito',
            name='estado',
            field=models.CharField(choices=[('Reservado', 'Reservado'), ('Completada', 'Completada'), ('Anulada', 'Anulada'), ('No asisten', 'No asisten')], max_length=50),
        ),
        migrations.AlterField(
            model_name='inscrito',
            name='institucion',
            field=models.CharField(choices=[('U Catolica', 'U Catolica'), ('U de Chile', 'U de Chile'), ('UFRO', 'UFRO'), ('Santo Tomas', 'Santo Tomas'), ('U Autonoma', 'U Autonoma'), ('Inacap', 'Inacap'), ('AIEP', 'AIEP')], max_length=50),
        ),
    ]
