# Generated by Django 3.2.23 on 2023-12-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_usuario_assistindo'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='dia_semana',
            field=models.CharField(choices=[('SEGUNDA', 'Segunda'), ('TERCA', 'Terca'), ('QUARTA', 'Quarta'), ('QUINTA', 'Quinta'), ('SEXTA', 'Sexta'), ('SABADO', 'Sabado'), ('DOMINGO', 'Domingo')], default='SEGUNDA', max_length=8),
        ),
    ]