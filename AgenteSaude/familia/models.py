
# -*- coding: utf-8 -*-
from django.db import models
from localflavor.br.br_states import STATE_CHOICES
from geoposition.fields import GeopositionField
from AgenteSaude.relatorio.models import *
from AgenteSaude.acompanhamento.models import *

import datetime


#classe para cadastrar o numero familia
class Cadastrar_Familia(models.Model):
	
	SITUACAO_IMOVEL_CHOICES =(
		(u'Alugada',u'ALUGADA'),
		(u'Propria',u'PROPRIA'),
		(u'Em Reforma',u'EM REFORMA'),
		(u'Abandonada',u'ABANDONADA'),
		(u'Em Construção',u'EM CONSTRUÇÃO'),
		(u'Fechada',u'FECHADA'),
	)

	TIPO_IMOVEL_CHOICES =(
		(u'Casa',u'CASA'),
		(u'Igreja',u'IGREJA'),
		(u'Apartamento',u'APARTAMENTO'),
		(u'Kitnet',u'kITNET'),
		(u'Bar',u'BAR'),
		(u'Terreno',u'TERRENO'),
		(u'Casa de Show',u'CASA DE SHOW'),
		(u'Restaurante',u'RESTAURANTE'),
		(u'Pizzaria',u'PIZZARIA'),
		(u'Padaria',u'PADARIA'),
		(u'Estadio de Futebol',u'ESTADIO DE FUTEBOL'),
	)

	CIDADE_CHOICES =(
		(u'Eunápolis',u'EUNÁPOLIS'),
	)

	
	def __unicode__(self):
		return unicode(self.NumeroFamilia_Descricao)	
	

	NumeroFamilia_id = models.AutoField(primary_key=True)
	NumeroFamilia_Responsavel = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nome do Responsável', help_text="Neste campo será cadastrado o nome do responsável")
	NumeroFamilia_Descricao = models.CharField(max_length=100,blank=True, null=True, verbose_name='Numero Familia', help_text="Neste campo será cadastrado o número da familia")
	NumeroFamilia_Cadastrado = models.IntegerField(blank=True, null=True, verbose_name='Número de pesssoas cadastrada',help_text="Neste campo será cadastrado a quantidade de pessoas cadastrada na Familia")
	NumeroFamilia_NaoCadastrado = models.IntegerField(blank=True, null=True, verbose_name='Número de pesssoas não cadastrada',help_text="Neste campo será cadastrado a quantidade de pessoas não cadastrada na Familia")
	NumeroFamilia_endereco_Rua = models.CharField(max_length=200, blank=True, null=True, verbose_name='Rua',help_text='Selecione a Rua correspondente do membro da família')
	NumeroFamilia_endereco_Numero = models.IntegerField(blank=True, null=True, verbose_name='Número da casa',help_text="Neste campo será cadastrado o número da casa")
	NumeroFamilia_endereco_Bairro = models.CharField(max_length=200, blank=True, null=True, verbose_name='Bairro',help_text='Selecione o Bairro correspondente do membro da família')
	NumeroFamilia_endereco_Cidade = models.CharField(max_length=200, blank=True, null=True, choices=CIDADE_CHOICES,verbose_name='Cidade',help_text='Selecione a cidade')
	NumeroFamilia_Endereco_Estado = models.CharField(max_length=25, null=True, choices=STATE_CHOICES, blank=True, verbose_name='Estado')
	NumeroFamiliaSituacaoImovel = models.CharField(max_length=25, blank=True,null=True, choices=SITUACAO_IMOVEL_CHOICES, verbose_name='Situação Imovel')
	NumeroFamiliatipoimovel = models.CharField(max_length=100, blank=True,null=True, verbose_name='Tipo de Imovel',choices=TIPO_IMOVEL_CHOICES,help_text='Selecione o tipo de Imóvel')


#classe para cadastrar as familias
class Cadastrar_Membro_Familia(models.Model):


	SEXO_CHOICES =(
		(u'M',u'Masculino'),
		(u'F',u'Feminino'),
	)

	DOENCA_CHOICES =(
		(u'Tuberculose',u'TUBERCULOSE'),
		(u'Hanseniase',u'HANSENIASE'),
		(u'Diabetico',u'DIABETICO'),
		(u'Hipertenso',u'HIPERTENSO'),
	)

	def __unicode__(self):
		return unicode(self.Familia_nome)


	Familia_id = models.AutoField(primary_key=True)
	Familia_Numero = models.ForeignKey(Cadastrar_Familia,verbose_name='Numero Familia',help_text='Selecione o número família correspondente')
	Familia_nome = models.CharField(max_length=200, blank=True, null=True, verbose_name='Nome', help_text='Informe o nome do membro da família')
	Familia_data_nascimento = models.DateField()
	Familia_idade = models.IntegerField(blank=True, null=True, verbose_name='Idade')
	Familia_sexo = models.CharField(max_length=50, blank=True, null=True,choices=SEXO_CHOICES,verbose_name='Sexo',help_text='Selecione o sexo do membro da família')
	Familia_numero_prontuario = models.IntegerField(blank=True, null=True, verbose_name='Numero Prontuario')
	Familia_endereco_Rua = models.CharField(max_length=200, blank=True, null=True, verbose_name='Rua',help_text='Nome da Rua')
	Familia_endereco_Numero = models.IntegerField(blank=True,null=True, verbose_name='Número', help_text='Número da casa')
	Familia_endereco_Bairro = models.CharField(max_length=200, blank=True, null=True, verbose_name='Bairro',help_text='Selecione o Bairro correspondente do membro da família')
	Familia_endereco_Cidade = models.CharField(max_length=200, blank=True, null=True, verbose_name='Cidade',help_text='Selecione a cidade')
	Familia_Endereco_Estado = models.CharField(max_length=25, null=True,blank=True, verbose_name='Estado')
   	Familia_Numero_SUS = models.IntegerField(blank=True,null=True,verbose_name='Numero do SUS')
	Familia_Gestante = models.BooleanField(verbose_name='Gestante', help_text="Marque esta opção caso seja uma Gestante")
	Familia_Hipertenso = models.BooleanField(verbose_name='Hipertenso', help_text="Marque esta opção caso seja um Hipertenso")
	Familia_Tuberculose = models.BooleanField(verbose_name='Tuberculose', help_text="Marque esta opção caso seja um Tuberculoso")
	Familia_Diabetico = models.BooleanField(verbose_name='Diabetico', help_text="Marque esta opção caso seja um Diabetico")
	Familia_Hanseniase = models.BooleanField(verbose_name='Hanseniase', help_text="Marque esta opção caso seja um Hanseniase")
	Familia_Medicamentos = models.TextField(verbose_name='Descricao dos medicamentos usados',blank=True, null=True)
	Familia_Numero_SUS = models.IntegerField(blank=True,null=True,verbose_name='Numero do SUS',help_text='Informe o número do SUS')
	Familia_Observacao = models.TextField(verbose_name='Observacoes diversas',blank=True,null=True)
	Familia_TipoDoenca = models.CharField(max_length=50,blank=True, null=True,choices=DOENCA_CHOICES,verbose_name='Tipo de Doenca',help_text='Selecione o tipo de doença')
	position = GeopositionField(verbose_name="Localização da Familia Cadastrada",blank=True,null=True,help_text='Informe o endereço para localizar a casa da familia que está sendo cadastrada')

	
	def Rua(self):
		rua = Cadastrar_Familia.objects.all().filter(NumeroFamilia_Descricao=self.Familia_Numero)
		self.Familia_endereco_Rua = rua[0].NumeroFamilia_endereco_Rua
		self.save()
		return self.Familia_endereco_Rua

	
	
	def Numero(self):
		numero = Cadastrar_Familia.objects.all().filter(NumeroFamilia_Descricao=self.Familia_Numero)
		self.Familia_endereco_Numero = numero[0].NumeroFamilia_endereco_Numero
		self.save()
		return self.Familia_endereco_Numero



	def Bairro(self):
		bairro = Cadastrar_Familia.objects.all().filter(NumeroFamilia_Descricao=self.Familia_Numero)
		self.Familia_endereco_Bairro = bairro[0].NumeroFamilia_endereco_Bairro
		self.save()
		return self.Familia_endereco_Bairro

		

	def Cidade(self):
		cidade = Cadastrar_Familia.objects.all().filter(NumeroFamilia_Descricao=self.Familia_Numero)
		self.Familia_endereco_Cidade = cidade[0].NumeroFamilia_endereco_Cidade
		self.save()
		return self.Familia_endereco_Cidade

	

	def Estado(self):
		estado = Cadastrar_Familia.objects.all().filter(NumeroFamilia_Descricao=self.Familia_Numero)
		self.Familia_Endereco_Estado = estado[0].NumeroFamilia_Endereco_Estado
		self.save()
		return self.Familia_Endereco_Estado

	
	def Idade(self):
		dataatual = datetime.date.today()
		self.Familia_idade = ((dataatual - self.Familia_data_nascimento).days / 365)
		self.save()
		return ((dataatual - self.Familia_data_nascimento).days / 365)

	def bucar_nome_doenca(self):
		resultado = Cadastrar_Familia.objects.all().filter(Familia_Hipertenso='Hipertenso')
		return resultado

