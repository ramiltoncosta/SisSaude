from django.shortcuts import render
from django.contrib import admin
from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader
from AgenteSaude.familia.models import *


def home(request):
	return render(request, 'index.html', {})

def endereco(request,ende):
	ender = Cadastrar_Familia.objects.all().filter(NumeroFamilia_endereco_Rua = ende)
	return render_to_response('relatorio_endereco.html',{'endereco':ender})