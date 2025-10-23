from django.shortcuts import render
from core.models import User

usuario = User.objects.all()

context = {
    'usuario':usuario
}
def organizador(requests):
    return render(requests, 'organizador.html', context)

