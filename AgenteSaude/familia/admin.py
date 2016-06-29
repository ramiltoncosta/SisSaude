
# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from AgenteSaude.familia.models import *
from AgenteSaude.relatorio.models import *
from AgenteSaude.acompanhamento.models import *


class Filtros(admin.SimpleListFilter):
	title = 'Idade menor ou igual a 2 anos'
	parameter_name = 'Familia_idade'

	def lookups(self, request, model_admin):
		return (
			(2, 'Menores de dois anos de idade'),
		)

	def queryset(self, request, queryset):

		if self.value():
			return queryset.filter(Familia_idade__lte=self.value())
		else:
			return queryset

class FamiliaForm(forms.ModelForm):
	class Media:
		css = {
		'all':('/static/css/geoposition.css',)
		}
		js = ('/static/js/geoposition_override.js',)


class Cadastrar_Membro_FamiliaAdmin(admin.ModelAdmin):
	form = FamiliaForm

	fieldsets = [
				 ('Dados Pessoais', {'fields': ['Familia_Numero','Familia_nome','Familia_data_nascimento','Familia_idade','Familia_sexo'], 'classes':['wide', 'extrapretty','collapse']}),
				 ('Informacoes Medicas',{'fields':['Familia_Hipertenso','Familia_Hanseniase','Familia_Diabetico','Familia_Tuberculose','Familia_Gestante','Familia_numero_prontuario','Familia_Numero_SUS','Familia_Medicamentos','Familia_Observacao'],'classes':['wide', 'extrapretty','collapse']}),
				 ('Endereco',{'fields':['Familia_endereco_Rua','Familia_endereco_Numero','Familia_endereco_Bairro','Familia_endereco_Cidade','Familia_Endereco_Estado'],'classes':['wide', 'extrapretty','collapse']}),
				 ('Informações da Localidade',{'fields':['position']}),
				]

	list_display = ['Familia_Numero','Familia_nome','Familia_data_nascimento','Idade','Familia_numero_prontuario','Rua','Numero','Bairro','Cidade','Estado','Familia_Numero_SUS','Familia_Medicamentos','Familia_Observacao']
	list_display_links = list_display
	list_filter = [Filtros,'Familia_endereco_Rua','Familia_Numero','Familia_Gestante','Familia_sexo','Familia_Numero']
	search_fields = ['Familia_nome','Familia_endereco_Rua','Familia_endereco_Cidade','Familia_Endereco_Estado']
	list_per_page = 10
	save_on_top = True
admin.site.register(Cadastrar_Membro_Familia,Cadastrar_Membro_FamiliaAdmin)


class Cadastrar_FamiliaAdmin(admin.ModelAdmin):
	model = Cadastrar_Familia
	fieldsets = [
				 ('Cadastro de Família', {'fields': ['NumeroFamilia_Responsavel','NumeroFamilia_Descricao','NumeroFamilia_endereco_Rua','NumeroFamilia_endereco_Bairro','NumeroFamilia_endereco_Numero'], 'classes':['wide', 'extrapretty','collapse']}),
				 ('Tipo Imóvel',{'fields':['NumeroFamiliatipoimovel','NumeroFamiliaSituacaoImovel','NumeroFamilia_Cadastrado','NumeroFamilia_NaoCadastrado'],'classes':['wide', 'extrapretty','collapse']}),
				 ('Outras Informações',{'fields':['NumeroFamilia_endereco_Cidade','NumeroFamilia_Endereco_Estado'],'classes':['wide', 'extrapretty','collapse']}),
				]

	list_display = ['NumeroFamilia_Descricao','NumeroFamilia_Cadastrado','NumeroFamilia_NaoCadastrado','NumeroFamilia_endereco_Rua','NumeroFamilia_endereco_Numero','NumeroFamilia_endereco_Bairro']
	list_display_links = list_display
	list_filter = ['NumeroFamilia_endereco_Rua']
	search_fields = ['NumeroFamilia_endereco_Rua','NumeroFamilia_endereco_Bairro','NumeroFamilia_endereco_Numero']
	list_per_page = 10
	save_on_top = True
admin.site.register(Cadastrar_Familia,Cadastrar_FamiliaAdmin)


class AcompanhanteGestanteAdmin(admin.ModelAdmin):
	model = AcompanhanteGestante
	fieldsets = [
				 ('Identificacao da Gestante', {'fields': ['NomeGestante','Acompanhante_Familia_Numero','AcompanhanteGestante_Rua','AcompanhanteGestante_Bairro'],'classes':['wide', 'extrapretty','collapse']}),
				 ('Data da Ultima Regra',{'fields':['AcompanhanteGestante_Data_Regra'],'classes':['wide', 'extrapretty']}),
				 ('Data Provavel do Parto',{'fields':['AcompanhanteGestante_Data_Parto'],'classes':['wide', 'extrapretty']}),
				 ('Data da Vacina',{'fields':['AcompanhanteGestante_Data_Vacina1','AcompanhanteGestante_Data_Vacina2','AcompanhanteGestante_Data_Vacina3','AcompanhanteGestante_Data_VacinaR'],'classes':['wide', 'extrapretty','collapse']}),
				 ('Estado Nucricional - D - Desnutrida e N - Nutrida',{'fields':['AcompanhanteGestante_EstadoNutricional'],'classes':['wide', 'extrapretty']}),
				 ('Data da Consulta do Pre Natal',{'fields':['AcompanhanteGestante_ConsultaPrenatal'],'classes':['wide', 'extrapretty']}),
				 ('Fatores de Riscos',{'fields':['AcompanhanteGestante_FatoresRiscos'],'classes':['wide', 'extrapretty']}),
				 ('Resultado da Gestacao',{'fields':['AcompanhanteGestante_NV','AcompanhanteGestante_NM','AcompanhanteGestante_AB'],'classes':['wide', 'extrapretty','collapse']}),
				 ('Data da Consulta do puerperio',{'fields':['AcompanhanteGestante_Perpetuo1','AcompanhanteGestante_Perpetuo2'],'classes':['wide', 'extrapretty','collapse']}),
				]

	list_display = ['NomeGestante','Acompanhante_Familia_Numero','Rua','Bairro','AcompanhanteGestante_Data_Regra','AcompanhanteGestante_Data_Parto','AcompanhanteGestante_Data_Vacina1','AcompanhanteGestante_Data_Vacina2','AcompanhanteGestante_Data_Vacina3','AcompanhanteGestante_Data_VacinaR','AcompanhanteGestante_EstadoNutricional','AcompanhanteGestante_ConsultaPrenatal','AcompanhanteGestante_NV','AcompanhanteGestante_NM','AcompanhanteGestante_AB','AcompanhanteGestante_Perpetuo1','AcompanhanteGestante_Perpetuo2']
	list_display_links = list_display
	list_filter = ['NomeGestante','Acompanhante_Familia_Numero','AcompanhanteGestante_Bairro']
	search_fields = ['NomeGestante__Familia_nome','Acompanhante_Familia_Numero__NumeroFamilia_Descricao','AcompanhanteGestante_Bairro']
	list_per_page = 10
	save_on_top = True

admin.site.register(AcompanhanteGestante,AcompanhanteGestanteAdmin)


class AcompanhanteHanseniaseAdmin(admin.ModelAdmin):
	model = AcompanhanteHanseniase
	fieldsets = [
				 ('Informações Gerais',{'fields':['NomeHanseniase','AcompanhanteHanseniase_DataNasc','AcompanhanteHanseniase_Idade','AcompanhanteHanseniase_Rua','AcompanhanteHanseniase_Numero'],'classes':['wide','extrapretty','collapse']}),
				 ('Outras Informações',{'fields':['AcompanhanteHanseniase_Informacoes']}),
	            ]
	list_display = ['NomeHanseniase','AcompanhanteHanseniase_DataNasc','AcompanhanteHanseniase_Idade','AcompanhanteHanseniase_Rua','AcompanhanteHanseniase_Numero']
	list_display_links = list_display
	list_filter = ['NomeHanseniase','AcompanhanteHanseniase_Rua']
	search_fields = ['AcompanhanteHanseniase_Rua']
	list_per_page = 10
	save_on_top = True
admin.site.register(AcompanhanteHanseniase,AcompanhanteHanseniaseAdmin)

class AcompanhanteTuberculoseAdmin(admin.ModelAdmin):
	model = AcompanhanteTuberculose
	fieldsets = [
				 ('Informações Gerais',{'fields':['NomeTuberculose','AcompanhanteTuberculose_DataNasc','AcompanhanteTuberculose_Idade','AcompanhanteTuberculose_Rua','AcompanhanteTuberculose_Numero'],'classes':['wide','extrapretty','collapse']}),
				 ('Outras Informações',{'fields':['AcompanhanteTuberculose_Informacoes']}),
	            ]
	list_display = ['NomeTuberculose','AcompanhanteTuberculose_DataNasc','AcompanhanteTuberculose_Idade','AcompanhanteTuberculose_Rua','AcompanhanteTuberculose_Numero']
	list_display_links = list_display
	list_filter = ['NomeTuberculose','AcompanhanteTuberculose_Rua']
	search_fields = ['AcompanhanteTuberculose_Rua']
	list_per_page = 10
	save_on_top = True
admin.site.register(AcompanhanteTuberculose,AcompanhanteTuberculoseAdmin)


class AcompanhanteDiabeticoAdmin(admin.ModelAdmin):
	model = AcompanhanteDiabetico
	fieldsets = [
				 ('Informações Gerais',{'fields':['NomeDiabetico','AcompanhanteDiabetico_DataNasc','AcompanhanteDiabetico_Idade','AcompanhanteDiabetico_Rua','AcompanhanteDiabetico_Numero'],'classes':['wide','extrapretty','collapse']}),
				 ('Outras Informações',{'fields':['AcompanhanteDiabetico_Informacoes']}),
	            ]
	list_display = ['NomeDiabetico','AcompanhanteDiabetico_DataNasc','AcompanhanteDiabetico_Idade','AcompanhanteDiabetico_Rua','AcompanhanteDiabetico_Numero']
	list_display_links = list_display
	list_filter = ['NomeDiabetico','AcompanhanteDiabetico_Rua']
	search_fields = ['AcompanhanteDiabetico_Rua']
	list_per_page = 10
	save_on_top = True
admin.site.register(AcompanhanteDiabetico,AcompanhanteDiabeticoAdmin)


class AcompanhanteHipertensoAdmin(admin.ModelAdmin):
	model = AcompanhanteHipertenso
	fieldsets = [
				 ('Informações Gerais',{'fields':['NomeHipertenso','AcompanhanteHipertenso_DataNasc','AcompanhanteHipertenso_Idade','AcompanhanteHipertenso_Rua','AcompanhanteHipertenso_Numero'],'classes':['wide','extrapretty','collapse']}),
				 ('Outras Informações',{'fields':['AcompanhanteHipertenso_Informacoes']}),
	            ]
	list_display = ['NomeHipertenso','AcompanhanteHipertenso_DataNasc','AcompanhanteHipertenso_Idade','AcompanhanteHipertenso_Rua','AcompanhanteHipertenso_Numero']
	list_display_links = list_display
	list_filter = ['NomeHipertenso','AcompanhanteHipertenso_Rua']
	search_fields = ['AcompanhanteHipertenso_Rua']
	list_per_page = 10
	save_on_top = True
admin.site.register(AcompanhanteHipertenso,AcompanhanteHipertensoAdmin)

class RelatorioTerritorialAdmin(admin.ModelAdmin):

	list_display = ['rua','quantidadecasa','quantidadeTerreno','quantidadeCasaEmConstrucao']
	list_filter = ['rua']

	lista_per_page = 10

admin.site.register(RelatorioTerritorial,RelatorioTerritorialAdmin)

class Rua_NumeroAdmin(admin.ModelAdmin):
	
	list_display=['rua','Numero_Casa']
	list_filter = ['rua']

	lista_per_page = 10

admin.site.register(Rua_Numero,Rua_NumeroAdmin)