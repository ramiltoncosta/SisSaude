# -*- coding: utf-8 -*-
from django.db import models
from django.db import models, migrations
from AgenteSaude.familia.models import *


class AcompanhanteGestante(models.Model):

	FATORES_CHOICES =(
		(u'6 ou mais gestações',u'6 OU MAIS GESTAÇÕES'),
		(u'Natimorto / Aborto',u'NATIMORTO / ABORTO'),
		(u'36 anos e mais',u'36 ANOS E MAIS'),
		(u'Menos de 20 anos',u'MENOS DE 20 ANOS'),
		(u'Sangramento',u'SANGRAMENTO'),
		(u'Edema',u'EDEMA'),
		(u'Diabetes',u'DIABETES'),
		(u'Pressão alta',u'PRESSÃO ALTA'),
	)


	AcompanhanteGestante_id = models.AutoField(primary_key=True)
	NomeGestante = models.OneToOneField(Cadastrar_Membro_Familia,verbose_name='Nome Gestante',help_text='Selecione o nome da Gestante')
	Acompanhante_Familia_Numero = models.ForeignKey(Cadastrar_Familia,blank=True, null=True,verbose_name='Número Família',help_text='Selecione o número da família que a gestante está cadastrada')
	AcompanhanteGestante_Rua = models.CharField(max_length=200,verbose_name='Rua',blank=True,null=True)
	AcompanhanteGestante_Bairro = models.CharField(max_length=200,verbose_name='Bairro',blank=True,null=True)
	AcompanhanteGestante_Data_Regra = models.DateField(verbose_name='Data',blank=True,null=True)
	AcompanhanteGestante_Data_Parto = models.DateField(verbose_name='Data',blank=True,null=True)
	AcompanhanteGestante_Data_Vacina1 = models.DateField(verbose_name='Vacina 1',blank=True,null=True)
	AcompanhanteGestante_Data_Vacina2 = models.DateField(verbose_name='Vacina 2',blank=True,null=True)
	AcompanhanteGestante_Data_Vacina3 = models.DateField(verbose_name='Vacina 3',blank=True,null=True)
	AcompanhanteGestante_Data_VacinaR = models.DateField(verbose_name='Vacina R',blank=True,null=True)
	AcompanhanteGestante_EstadoNutricional = models.TextField(verbose_name='Estado Nutricional',blank=True,null=True)
	AcompanhanteGestante_ConsultaPrenatal = models.TextField(verbose_name='Informe dados sobre a consulta de pre-natal',blank=True,null=True)
	AcompanhanteGestante_FatoresRiscos = models.CharField(max_length=50,blank=True, null=True,choices=FATORES_CHOICES,verbose_name='Fatores de Riscos')
	AcompanhanteGestante_NV = models.DateField(verbose_name='Nascidos Vivos',blank=True,null=True)
	AcompanhanteGestante_NM = models.DateField(verbose_name='Nascidos Mortos',blank=True,null=True)
	AcompanhanteGestante_AB = models.DateField(verbose_name='Aborto',blank=True,null=True)
	AcompanhanteGestante_Perpetuo1 = models.DateField(verbose_name='Primeira Consulta',blank=True,null=True)
	AcompanhanteGestante_Perpetuo2 = models.DateField(verbose_name='Segunda Consulta',blank=True,null=True)

	
	def Rua(self):
		rua = Cadastrar_Membro_Familia.objects.all().filter(Familia_nome=self.NomeGestante).filter(Familia_Numero=self.Acompanhante_Familia_Numero)
		self.AcompanhanteGestante_Rua = rua[0].Familia_endereco_Rua
		self.save()
		return self.AcompanhanteGestante_Rua

	

	def Bairro(self):
		bairro = Cadastrar_Membro_Familia.objects.all().filter(Familia_nome=self.NomeGestante).filter(Familia_Numero=self.Acompanhante_Familia_Numero)
		self.AcompanhanteGestante_Bairro = bairro[0].Familia_endereco_Bairro
		self.save()
		return self.AcompanhanteGestante_Bairro


	class Meta:
		verbose_name, verbose_name_plural = u"AcompanhanteGestante" , u"AcompanhanteGestantes"
		ordering = ('NomeGestante',)


#classe para cadastrar o acompanhamento de hipertenso
class AcompanhanteHipertenso(models.Model):


	AcompanhanteHipertenso_id = models.AutoField(primary_key=True)
	NomeHipertenso = models.OneToOneField(Cadastrar_Membro_Familia,verbose_name='Nome',help_text='Selecione o nome')
	AcompanhanteHipertenso_DataNasc = models.CharField(max_length=20)
	AcompanhanteHipertenso_Idade = models.IntegerField(verbose_name='Idade',blank=True,null=True,help_text='Selecione a idade do Hipertenso')
	AcompanhanteHipertenso_Rua = models.CharField(max_length=200,verbose_name='Rua',blank=True,null=True)
	AcompanhanteHipertenso_Numero = models.CharField(max_length=200,verbose_name='Rua',blank=True,null=True)
	AcompanhanteHipertenso_Informacoes = models.TextField()
	
	

	def Rua(self):
		rua = Cadastrar_Membro_Familia.objects.all().filter(Familia_nome=self.NomeHipertenso)
		self.AcompanhanteHipertenso_Rua = rua[0].Familia_endereco_Rua
		self.save()
		return self.AcompanhanteHipertenso_Rua

	

	def Idade(self):
		idade = Cadastrar_Membro_Familia.objects.all().filter(Familia_nome=self.NomeHipertenso)
		self.AcompanhanteHipertenso_Idade = idade[0].Familia_idade
		self.save()
		return self.AcompanhanteHipertenso_Idade

	class Meta:
		verbose_name, verbose_name_plural = u"AcompanhanteHipertenso" , u"AcompanhanteHipertensos"
		ordering = ('NomeHipertenso',)

	
#classe para cadastrar o acompanhamento de hanseníase
class AcompanhanteHanseniase(models.Model):

	
	AcompanhanteHanseniase_id = models.AutoField(primary_key=True)
	NomeHanseniase = models.OneToOneField(Cadastrar_Membro_Familia,verbose_name='Nome',help_text='Selecione o nome')
	AcompanhanteHanseniase_DataNasc = models.CharField(max_length=20)
	AcompanhanteHanseniase_Idade = models.IntegerField(verbose_name='Idade',blank=True,null=True,help_text='Selecione a idade do Hipertenso')
	AcompanhanteHanseniase_Rua = models.CharField(max_length=200,verbose_name='Rua',blank=True,null=True)
	AcompanhanteHanseniase_Numero = models.CharField(max_length=200,verbose_name='Número',blank=True,null=True)
	AcompanhanteHanseniase_Informacoes = models.TextField()
	

	def Rua(self):
		rua = Cadastrar_Membro_Familia.objects.all().filter(Familia_nome=self.NomeHanseniase)
		self.AcompanhanteHanseniase_Rua = rua[0].Familia_endereco_Rua
		self.save()
		return self.AcompanhanteHanseniase_Rua
	

	def Idade(self):
		idade = Cadastrar_Membro_Familia.objects.all().filter(Familia_nome=self.NomeHanseniase)
		self.AcompanhanteHanseniase_Idade = idade[0].Familia_idade
		self.save()
		return self.AcompanhanteHanseniase_Idade

	class Meta:
		verbose_name, verbose_name_plural = u"AcompanhanteHanseniase" , u"AcompanhanteHanseniases"
		ordering = ('NomeHanseniase',)

#classe para cadastrar o acompanhamento de tuberculose
class AcompanhanteTuberculose(models.Model):

	
	AcompanhanteTuberculose_id = models.AutoField(primary_key=True)
	NomeTuberculose = models.OneToOneField(Cadastrar_Membro_Familia,verbose_name='Nome',help_text='Selecione o nome')
	AcompanhanteTuberculose_DataNasc = models.CharField(max_length=20)
	AcompanhanteTuberculose_Idade = models.IntegerField(verbose_name='Idade',blank=True,null=True,help_text='Selecione a idade do Hipertenso')
	AcompanhanteTuberculose_Rua = models.CharField(max_length=200,verbose_name='Rua',blank=True,null=True)
	AcompanhanteTuberculose_Numero = models.CharField(max_length=200,verbose_name='Número',blank=True,null=True)
	AcompanhanteTuberculose_Informacoes = models.TextField()
	
	def Rua(self):
		rua = Cadastrar_Membro_Familia.objects.all().filter(Familia_nome=self.NomeTuberculose)
		self.AcompanhanteTuberculose_Rua = rua[0].Familia_endereco_Rua
		self.save()
		return self.AcompanhanteTuberculose_Rua

	
	def Idade(self):
		idade = Cadastrar_Membro_Familia.objects.all().filter(Familia_nome=self.NomeTuberculose)
		self.AcompanhanteTuberculose_Idade = idade[0].Familia_idade
		self.save()
		return self.AcompanhanteTuberculose_Idade

	class Meta:
		verbose_name, verbose_name_plural = u"AcompanhanteTuberculose" , u"AcompanhanteTuberculoses"
		ordering = ('NomeTuberculose',)

#classe para cadastrar o acompanhamento de diabetico
class AcompanhanteDiabetico(models.Model):


	AcompanhanteDiabetico_id = models.AutoField(primary_key=True)
	NomeDiabetico = models.OneToOneField(Cadastrar_Membro_Familia,verbose_name='Nome',help_text='Selecione o nome')
	AcompanhanteDiabetico_DataNasc = models.CharField(max_length=20)
	AcompanhanteDiabetico_Idade = models.IntegerField(verbose_name='Idade',blank=True,null=True,help_text='Selecione a idade do Hipertenso')
	AcompanhanteDiabetico_Rua = models.CharField(max_length=200,verbose_name='Rua',blank=True,null=True)
	AcompanhanteDiabetico_Numero = models.CharField(max_length=200,verbose_name='Número',blank=True,null=True)
	AcompanhanteDiabetico_Informacoes = models.TextField()
	
	

	def Rua(self):
		rua = Cadastrar_Membro_Familia.objects.all().filter(Familia_nome=self.NomeDiabetico)
		self.AcompanhanteDiabetico_Rua = rua[0].Familia_endereco_Rua
		self.save()
		return self.AcompanhanteDiabetico_Rua

	

	def Idade(self):
		idade = Cadastrar_Membro_Familia.objects.all().filter(Familia_nome=self.NomeDiabetico)
		self.AcompanhanteDiabetico_Idade = idade[0].Familia_idade
		self.save()
		return self.AcompanhanteDiabetico_Idade

	class Meta:
		verbose_name, verbose_name_plural = u"AcompanhanteDiabetico" , u"AcompanhanteDiabeticos"
		ordering = ('NomeDiabetico',)
			