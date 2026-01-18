from django.shortcuts import render

def sortear (request):
    return render(request, "sorteo/sorteo.html")
    
def sorteados (request):
    return render(request, "sorteo/sorteados.html")