# -*- coding: utf-8 -*-
from django.db import models
from django.db import models, migrations
from django.db.models import Sum
from AgenteSaude.acompanhamento.models import *
from AgenteSaude.familia.models import *


class RelatorioTerritorial(models.Model):
	
	rua = models.CharField(max_length=200,unique=True,blank=True,null=True,help_text="Informe o endereço para a gerar o relatório territorial")
	

	def quantidadecasa(self):

		rua = Cadastrar_Familia.objects.all().filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamiliatipoimovel="Casa")
		resultado = rua.count()
		return resultado

	def quantidadeapartamento(self):

		rua = Cadastrar_Familia.objects.all().filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamiliatipoimovel="Apartamento")
		resultado = rua.count()
		return resultado

	def quantidadeFamilia(self):
		rua = Cadastrar_Familia.objects.all().filter(NumeroFamilia_endereco_Rua=self.rua)
		resultado = rua.count()
		return resultado

	def quantidadeTerreno(self):
		result = Cadastrar_Familia.objects.all().filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamiliatipoimovel="Terreno")
		resultado = result.count()
		return resultado

	def quantidadeBar(self):
		result = Cadastrar_Familia.objects.all().filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamiliatipoimovel="Bar")
		resultado = result.count()
		return resultado


	def quantidadeIgreja(self):
		result = Cadastrar_Familia.objects.all().filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamiliatipoimovel="Igreja")
		resultado = result.count()
		return resultado


	def quantidadeCasaAlugada(self):
		result = Cadastrar_Familia.objects.all().filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamiliaSituacaoImovel="Alugada")
		resultado = result.count()
		return resultado

	def quantidadeCasaPropria(self):
		result = Cadastrar_Familia.objects.all().filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamiliaSituacaoImovel="Propria")
		resultado = result.count()
		return resultado


	def quantidadeCasaFechada(self):
		result = Cadastrar_Familia.objects.all().filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamiliaSituacaoImovel="Fechada")
		resultado = result.count()
		return resultado

	def quantidadeCasaPropria(self):
		result = Cadastrar_Familia.objects.all().filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamiliaSituacaoImovel="Propria")
		resultado = result.count()
		return resultado

	def quantidadeCasaEmReforma(self):
		result = Cadastrar_Familia.objects.all().filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamiliaSituacaoImovel="Em Reforma")
		resultado = result.count()
		return resultado

	def quantidadeCasaAbandonada(self):
		result = Cadastrar_Familia.objects.all().filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamiliaSituacaoImovel="Abandonada")
		resultado = result.count()
		return resultado

	def quantidadeCasaEmConstrucao(self):
		result = Cadastrar_Familia.objects.all().filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamiliaSituacaoImovel="Em Construção")
		resultado = result.count()
		return resultado

	def quantidadepessoasnaocadastradas(self):
		result = Cadastrar_Familia.objects.filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamilia_NaoCadastrado__gte=0)
		resultado = result.aggregate(Total=Sum('NumeroFamilia_NaoCadastrado'))
		res = resultado['Total']
		return res


	def quantidadepessoascadastradas(self):
		result = Cadastrar_Familia.objects.filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamilia_Cadastrado__gte=1)
		resultado = result.aggregate(Total=Sum('NumeroFamilia_Cadastrado'))
		res = resultado['Total']
		return res


	#def quantidadetotalpessoa(self):
	#	result1 = Cadastrar_Familia.objects.filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamilia_Cadastrado__gte=1)
	#	result2 = Cadastrar_Familia.objects.filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamilia_NaoCadastrado__gte=0)
	#	resultado1 = result1.aggregate(Total=Sum('NumeroFamilia_Cadastrado'))
	#	resultado2 = result2.aggregate(Total=Sum('NumeroFamilia_NaoCadastrado'))
	#	res1 = resultado1['Total']
	#	res2 = resultado2['Total']
	#	resultadogeral = 0
	#	resultadogeral = res1 + res2
	#	return resultadogeral


class Rua_Numero(models.Model):

	rua = models.CharField(max_length=200,unique=True,blank=True,null=True,help_text="Informe o endereço para a gerar o relatório territorial")


	def Numero_Casa(self):
		result = Cadastrar_Familia.objects.filter(NumeroFamilia_endereco_Rua=self.rua).filter(NumeroFamilia_Cadastrado__gte=1)
		numerorua = result[0].NumeroFamilia_endereco_Numero
		quantpessoa = Cadastrar_Familia.objects.filter(NumeroFamilia_endereco_Numero=numerorua)
		quanp = quantpessoa[0].NumeroFamilia_Cadastrado
		return quanp