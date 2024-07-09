from django.shortcuts import render
from .models import Paste


def index(request):
    pastes = Paste.objects.all()

    context = {
        'pastes': pastes,
    }

    return render(request, 'app_pastebin/index.html', context=context)


def new_paste(request):

    context = {}

    return render(request, 'app_pastebin/new_paste.html', context=context)
