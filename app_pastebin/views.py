from django.shortcuts import render, redirect
from .models import Paste
from .forms import CreatePasteForm
from pygments.formatters import HtmlFormatter


def index(request):
    pastes = Paste.objects.all()

    context = {
        'pastes': pastes,
    }

    return render(request, 'app_pastebin/index.html', context=context)


def new_paste(request):
    if request.method == "POST":
        form = CreatePasteForm(request.POST)

        if form.is_valid():
            new_paste = form.save(commit=False)
            
            # other any logics may write here

            new_paste.save()
            return redirect('index')
    else:
        form = CreatePasteForm()

    context = {
        'title': 'Create Paste',
        'form': form,
    }


    return render(request, 'app_pastebin/new_paste.html', context=context)
