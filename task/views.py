from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

class Tarefa(object):
	"""docstring for ClassName"""
	def __init__(self, titulo, data):
		self.titulo = titulo
		self.data = data
	def __str__(self):
		return self.info
		

def home(request):
    return HttpResponse("Olá")
def sobre(request):
    return HttpResponse("Taylor Oliveira")
def tarefa(request, numero):
	return HttpResponse("Terefa:" + str(numero))
def tarefa(request, ano, mes, dia):
	return HttpResponse("Terefa:" + str(ano) + " " + str(mes) + " " + str(dia))