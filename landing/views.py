from django.shortcuts import render
from .forms import GamersForm


def landing(request):
    form = GamersForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        gamer_in = form.cleaned_data
        #перевіряю чи gamer_in["login"] є в таблиці Gamers
        #якщо так, переходжу на сторінку game
        #якщо ні видаю повідомлення: "Користувач не ідентифікований"

    return render(request, 'landing/landing.html', locals())