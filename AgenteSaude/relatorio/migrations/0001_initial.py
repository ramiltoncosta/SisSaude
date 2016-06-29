# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RelatorioTerritorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rua', models.CharField(help_text=b'Informe o endere\xc3\xa7o para a gerar o relat\xc3\xb3rio territorial', max_length=200, unique=True, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rua_Numero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rua', models.CharField(help_text=b'Informe o endere\xc3\xa7o para a gerar o relat\xc3\xb3rio territorial', max_length=200, unique=True, null=True, blank=True)),
            ],
        ),
    ]
