# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastrar_Familia',
            fields=[
                ('NumeroFamilia_id', models.AutoField(serialize=False, primary_key=True)),
                ('NumeroFamilia_Responsavel', models.CharField(help_text=b'Neste campo ser\xc3\xa1 cadastrado o nome do respons\xc3\xa1vel', max_length=100, null=True, verbose_name=b'Nome do Respons\xc3\xa1vel', blank=True)),
                ('NumeroFamilia_Descricao', models.CharField(help_text=b'Neste campo ser\xc3\xa1 cadastrado o n\xc3\xbamero da familia', max_length=100, null=True, verbose_name=b'Numero Familia', blank=True)),
                ('NumeroFamilia_Cadastrado', models.IntegerField(help_text=b'Neste campo ser\xc3\xa1 cadastrado a quantidade de pessoas cadastrada na Familia', null=True, verbose_name=b'N\xc3\xbamero de pesssoas cadastrada', blank=True)),
                ('NumeroFamilia_NaoCadastrado', models.IntegerField(help_text=b'Neste campo ser\xc3\xa1 cadastrado a quantidade de pessoas n\xc3\xa3o cadastrada na Familia', null=True, verbose_name=b'N\xc3\xbamero de pesssoas n\xc3\xa3o cadastrada', blank=True)),
                ('NumeroFamilia_endereco_Rua', models.CharField(help_text=b'Selecione a Rua correspondente do membro da fam\xc3\xadlia', max_length=200, null=True, verbose_name=b'Rua', blank=True)),
                ('NumeroFamilia_endereco_Numero', models.IntegerField(help_text=b'Neste campo ser\xc3\xa1 cadastrado o n\xc3\xbamero da casa', null=True, verbose_name=b'N\xc3\xbamero da casa', blank=True)),
                ('NumeroFamilia_endereco_Bairro', models.CharField(help_text=b'Selecione o Bairro correspondente do membro da fam\xc3\xadlia', max_length=200, null=True, verbose_name=b'Bairro', blank=True)),
                ('NumeroFamilia_endereco_Cidade', models.CharField(choices=[('Eun\xe1polis', 'EUN\xc1POLIS')], max_length=200, blank=True, help_text=b'Selecione a cidade', null=True, verbose_name=b'Cidade')),
                ('NumeroFamilia_Endereco_Estado', models.CharField(blank=True, max_length=25, null=True, verbose_name=b'Estado', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('NumeroFamiliaSituacaoImovel', models.CharField(blank=True, max_length=25, null=True, verbose_name=b'Situa\xc3\xa7\xc3\xa3o Imovel', choices=[('Alugada', 'ALUGADA'), ('Propria', 'PROPRIA'), ('Em Reforma', 'EM REFORMA'), ('Abandonada', 'ABANDONADA'), ('Em Constru\xe7\xe3o', 'EM CONSTRU\xc7\xc3O'), ('Fechada', 'FECHADA')])),
                ('NumeroFamiliatipoimovel', models.CharField(choices=[('Casa', 'CASA'), ('Igreja', 'IGREJA'), ('Apartamento', 'APARTAMENTO'), ('Kitnet', 'kITNET'), ('Bar', 'BAR'), ('Terreno', 'TERRENO'), ('Casa de Show', 'CASA DE SHOW'), ('Restaurante', 'RESTAURANTE'), ('Pizzaria', 'PIZZARIA'), ('Padaria', 'PADARIA'), ('Estadio de Futebol', 'ESTADIO DE FUTEBOL')], max_length=100, blank=True, help_text=b'Selecione o tipo de Im\xc3\xb3vel', null=True, verbose_name=b'Tipo de Imovel')),
            ],
        ),
        migrations.CreateModel(
            name='Cadastrar_Membro_Familia',
            fields=[
                ('Familia_id', models.AutoField(serialize=False, primary_key=True)),
                ('Familia_nome', models.CharField(help_text=b'Informe o nome do membro da fam\xc3\xadlia', max_length=200, null=True, verbose_name=b'Nome', blank=True)),
                ('Familia_data_nascimento', models.DateField()),
                ('Familia_idade', models.IntegerField(null=True, verbose_name=b'Idade', blank=True)),
                ('Familia_sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=50, blank=True, help_text=b'Selecione o sexo do membro da fam\xc3\xadlia', null=True, verbose_name=b'Sexo')),
                ('Familia_numero_prontuario', models.IntegerField(null=True, verbose_name=b'Numero Prontuario', blank=True)),
                ('Familia_endereco_Rua', models.CharField(help_text=b'Nome da Rua', max_length=200, null=True, verbose_name=b'Rua', blank=True)),
                ('Familia_endereco_Numero', models.IntegerField(help_text=b'N\xc3\xbamero da casa', null=True, verbose_name=b'N\xc3\xbamero', blank=True)),
                ('Familia_endereco_Bairro', models.CharField(help_text=b'Selecione o Bairro correspondente do membro da fam\xc3\xadlia', max_length=200, null=True, verbose_name=b'Bairro', blank=True)),
                ('Familia_endereco_Cidade', models.CharField(help_text=b'Selecione a cidade', max_length=200, null=True, verbose_name=b'Cidade', blank=True)),
                ('Familia_Endereco_Estado', models.CharField(max_length=25, null=True, verbose_name=b'Estado', blank=True)),
                ('Familia_Gestante', models.BooleanField(help_text=b'Marque esta op\xc3\xa7\xc3\xa3o caso seja uma Gestante', verbose_name=b'Gestante')),
                ('Familia_Hipertenso', models.BooleanField(help_text=b'Marque esta op\xc3\xa7\xc3\xa3o caso seja um Hipertenso', verbose_name=b'Hipertenso')),
                ('Familia_Tuberculose', models.BooleanField(help_text=b'Marque esta op\xc3\xa7\xc3\xa3o caso seja um Tuberculoso', verbose_name=b'Tuberculose')),
                ('Familia_Diabetico', models.BooleanField(help_text=b'Marque esta op\xc3\xa7\xc3\xa3o caso seja um Diabetico', verbose_name=b'Diabetico')),
                ('Familia_Hanseniase', models.BooleanField(help_text=b'Marque esta op\xc3\xa7\xc3\xa3o caso seja um Hanseniase', verbose_name=b'Hanseniase')),
                ('Familia_Medicamentos', models.TextField(null=True, verbose_name=b'Descricao dos medicamentos usados', blank=True)),
                ('Familia_Numero_SUS', models.IntegerField(help_text=b'Informe o n\xc3\xbamero do SUS', null=True, verbose_name=b'Numero do SUS', blank=True)),
                ('Familia_Observacao', models.TextField(null=True, verbose_name=b'Observacoes diversas', blank=True)),
                ('Familia_TipoDoenca', models.CharField(choices=[('Tuberculose', 'TUBERCULOSE'), ('Hanseniase', 'HANSENIASE'), ('Diabetico', 'DIABETICO'), ('Hipertenso', 'HIPERTENSO')], max_length=50, blank=True, help_text=b'Selecione o tipo de doen\xc3\xa7a', null=True, verbose_name=b'Tipo de Doenca')),
                ('position', geoposition.fields.GeopositionField(help_text=b'Informe o endere\xc3\xa7o para localizar a casa da familia que est\xc3\xa1 sendo cadastrada', max_length=42, null=True, verbose_name=b'Localiza\xc3\xa7\xc3\xa3o da Familia Cadastrada', blank=True)),
                ('Familia_Numero', models.ForeignKey(verbose_name=b'Numero Familia', to='familia.Cadastrar_Familia', help_text=b'Selecione o n\xc3\xbamero fam\xc3\xadlia correspondente')),
            ],
        ),
    ]
