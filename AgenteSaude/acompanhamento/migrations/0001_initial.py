# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcompanhanteDiabetico',
            fields=[
                ('AcompanhanteDiabetico_id', models.AutoField(serialize=False, primary_key=True)),
                ('AcompanhanteDiabetico_DataNasc', models.CharField(max_length=20)),
                ('AcompanhanteDiabetico_Idade', models.IntegerField(help_text=b'Selecione a idade do Hipertenso', null=True, verbose_name=b'Idade', blank=True)),
                ('AcompanhanteDiabetico_Rua', models.CharField(max_length=200, null=True, verbose_name=b'Rua', blank=True)),
                ('AcompanhanteDiabetico_Numero', models.CharField(max_length=200, null=True, verbose_name=b'N\xc3\xbamero', blank=True)),
                ('AcompanhanteDiabetico_Informacoes', models.TextField()),
                ('NomeDiabetico', models.OneToOneField(verbose_name=b'Nome', to='familia.Cadastrar_Membro_Familia', help_text=b'Selecione o nome')),
            ],
            options={
                'ordering': ('NomeDiabetico',),
                'verbose_name': 'AcompanhanteDiabetico',
                'verbose_name_plural': 'AcompanhanteDiabeticos',
            },
        ),
        migrations.CreateModel(
            name='AcompanhanteGestante',
            fields=[
                ('AcompanhanteGestante_id', models.AutoField(serialize=False, primary_key=True)),
                ('AcompanhanteGestante_Rua', models.CharField(max_length=200, null=True, verbose_name=b'Rua', blank=True)),
                ('AcompanhanteGestante_Bairro', models.CharField(max_length=200, null=True, verbose_name=b'Bairro', blank=True)),
                ('AcompanhanteGestante_Data_Regra', models.DateField(null=True, verbose_name=b'Data', blank=True)),
                ('AcompanhanteGestante_Data_Parto', models.DateField(null=True, verbose_name=b'Data', blank=True)),
                ('AcompanhanteGestante_Data_Vacina1', models.DateField(null=True, verbose_name=b'Vacina 1', blank=True)),
                ('AcompanhanteGestante_Data_Vacina2', models.DateField(null=True, verbose_name=b'Vacina 2', blank=True)),
                ('AcompanhanteGestante_Data_Vacina3', models.DateField(null=True, verbose_name=b'Vacina 3', blank=True)),
                ('AcompanhanteGestante_Data_VacinaR', models.DateField(null=True, verbose_name=b'Vacina R', blank=True)),
                ('AcompanhanteGestante_EstadoNutricional', models.TextField(null=True, verbose_name=b'Estado Nutricional', blank=True)),
                ('AcompanhanteGestante_ConsultaPrenatal', models.TextField(null=True, verbose_name=b'Informe dados sobre a consulta de pre-natal', blank=True)),
                ('AcompanhanteGestante_FatoresRiscos', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Fatores de Riscos', choices=[('6 ou mais gesta\xe7\xf5es', '6 OU MAIS GESTA\xc7\xd5ES'), ('Natimorto / Aborto', 'NATIMORTO / ABORTO'), ('36 anos e mais', '36 ANOS E MAIS'), ('Menos de 20 anos', 'MENOS DE 20 ANOS'), ('Sangramento', 'SANGRAMENTO'), ('Edema', 'EDEMA'), ('Diabetes', 'DIABETES'), ('Press\xe3o alta', 'PRESS\xc3O ALTA')])),
                ('AcompanhanteGestante_NV', models.DateField(null=True, verbose_name=b'Nascidos Vivos', blank=True)),
                ('AcompanhanteGestante_NM', models.DateField(null=True, verbose_name=b'Nascidos Mortos', blank=True)),
                ('AcompanhanteGestante_AB', models.DateField(null=True, verbose_name=b'Aborto', blank=True)),
                ('AcompanhanteGestante_Perpetuo1', models.DateField(null=True, verbose_name=b'Primeira Consulta', blank=True)),
                ('AcompanhanteGestante_Perpetuo2', models.DateField(null=True, verbose_name=b'Segunda Consulta', blank=True)),
                ('Acompanhante_Familia_Numero', models.ForeignKey(blank=True, to='familia.Cadastrar_Familia', help_text=b'Selecione o n\xc3\xbamero da fam\xc3\xadlia que a gestante est\xc3\xa1 cadastrada', null=True, verbose_name=b'N\xc3\xbamero Fam\xc3\xadlia')),
                ('NomeGestante', models.OneToOneField(verbose_name=b'Nome Gestante', to='familia.Cadastrar_Membro_Familia', help_text=b'Selecione o nome da Gestante')),
            ],
            options={
                'ordering': ('NomeGestante',),
                'verbose_name': 'AcompanhanteGestante',
                'verbose_name_plural': 'AcompanhanteGestantes',
            },
        ),
        migrations.CreateModel(
            name='AcompanhanteHanseniase',
            fields=[
                ('AcompanhanteHanseniase_id', models.AutoField(serialize=False, primary_key=True)),
                ('AcompanhanteHanseniase_DataNasc', models.CharField(max_length=20)),
                ('AcompanhanteHanseniase_Idade', models.IntegerField(help_text=b'Selecione a idade do Hipertenso', null=True, verbose_name=b'Idade', blank=True)),
                ('AcompanhanteHanseniase_Rua', models.CharField(max_length=200, null=True, verbose_name=b'Rua', blank=True)),
                ('AcompanhanteHanseniase_Numero', models.CharField(max_length=200, null=True, verbose_name=b'N\xc3\xbamero', blank=True)),
                ('AcompanhanteHanseniase_Informacoes', models.TextField()),
                ('NomeHanseniase', models.OneToOneField(verbose_name=b'Nome', to='familia.Cadastrar_Membro_Familia', help_text=b'Selecione o nome')),
            ],
            options={
                'ordering': ('NomeHanseniase',),
                'verbose_name': 'AcompanhanteHanseniase',
                'verbose_name_plural': 'AcompanhanteHanseniases',
            },
        ),
        migrations.CreateModel(
            name='AcompanhanteHipertenso',
            fields=[
                ('AcompanhanteHipertenso_id', models.AutoField(serialize=False, primary_key=True)),
                ('AcompanhanteHipertenso_DataNasc', models.CharField(max_length=20)),
                ('AcompanhanteHipertenso_Idade', models.IntegerField(help_text=b'Selecione a idade do Hipertenso', null=True, verbose_name=b'Idade', blank=True)),
                ('AcompanhanteHipertenso_Rua', models.CharField(max_length=200, null=True, verbose_name=b'Rua', blank=True)),
                ('AcompanhanteHipertenso_Numero', models.CharField(max_length=200, null=True, verbose_name=b'Rua', blank=True)),
                ('AcompanhanteHipertenso_Informacoes', models.TextField()),
                ('NomeHipertenso', models.OneToOneField(verbose_name=b'Nome', to='familia.Cadastrar_Membro_Familia', help_text=b'Selecione o nome')),
            ],
            options={
                'ordering': ('NomeHipertenso',),
                'verbose_name': 'AcompanhanteHipertenso',
                'verbose_name_plural': 'AcompanhanteHipertensos',
            },
        ),
        migrations.CreateModel(
            name='AcompanhanteTuberculose',
            fields=[
                ('AcompanhanteTuberculose_id', models.AutoField(serialize=False, primary_key=True)),
                ('AcompanhanteTuberculose_DataNasc', models.CharField(max_length=20)),
                ('AcompanhanteTuberculose_Idade', models.IntegerField(help_text=b'Selecione a idade do Hipertenso', null=True, verbose_name=b'Idade', blank=True)),
                ('AcompanhanteTuberculose_Rua', models.CharField(max_length=200, null=True, verbose_name=b'Rua', blank=True)),
                ('AcompanhanteTuberculose_Numero', models.CharField(max_length=200, null=True, verbose_name=b'N\xc3\xbamero', blank=True)),
                ('AcompanhanteTuberculose_Informacoes', models.TextField()),
                ('NomeTuberculose', models.OneToOneField(verbose_name=b'Nome', to='familia.Cadastrar_Membro_Familia', help_text=b'Selecione o nome')),
            ],
            options={
                'ordering': ('NomeTuberculose',),
                'verbose_name': 'AcompanhanteTuberculose',
                'verbose_name_plural': 'AcompanhanteTuberculoses',
            },
        ),
    ]
