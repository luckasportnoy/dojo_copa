from django.shortcuts import render, HttpResponseRedirect
from copa.models import Jogos

def listaJogo(request):
	jogo=Jogos.objects.all()
	return render(request, 'copa.html', {'jogo':jogo})

def salvar(request):
	time1 = request.POST.get('time1')
	score1 = request.POST.get('score1')
	time2 = request.POST.get('time2')
	score2 = request.POST.get('score2')

	jogo = Jogos(time1=time1, score2=score2, time2=time2, score1=score1)
	jogo.save()
	return listaJogo(request)



