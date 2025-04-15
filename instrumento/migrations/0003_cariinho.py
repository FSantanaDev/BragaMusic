# Generated by Django 5.1.7 on 2025-03-11 13:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrumento', '0002_cliente_nome_completo'),
    ]

    operations = [
        migrations.CreateModel(
            name='cariinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
                ('instrumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instrumento.instrumento', verbose_name='Instrumento')),
            ],
        ),
    ]
