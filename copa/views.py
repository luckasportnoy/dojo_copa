from django.shortcuts import render

def listaJogo(request):
	return render(request, 'copa.html')
