# Generated by Django 3.2.3 on 2021-06-12 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contacto',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de contacto'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fecha_nacimiento',
            field=models.DateField(null=True, verbose_name='Fecha nacimiento usuario'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sexo',
            field=models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer'), ('O', 'Otro')], max_length=1, null=True, verbose_name='Sexo usuario'),
        ),
    ]
