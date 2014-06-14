from django.shortcuts import render, HttpResponseRedirect
from copa.models import Jogos

def listarJogo(request):
  jogo = Jogos.objects.all()
  return render(request, 'copa.html', {'jogo':jogo})

def salvar(request):
  score1 = request.POST.get('score1')
  score2 = request.POST.get('score2')
  score3 = request.POST.get('score3')
  score4 = request.POST.get('score4')
  score5 = request.POST.get('score5')
  score6 = request.POST.get('score6')

  jogo = Jogos(score1=score1, score2=score2, score3=score3, score4=score4, score5=score5, score6=score6)
  jogo.save()

  return listarJogo(request)



