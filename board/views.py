from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Bulletin


def home(request):
    bulletins = Bulletin.objects
    return render(request, '../templates/board/home.html', {'bulletins': bulletins})


@login_required()
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['text'] or request.POST['url'] or request.FILES['image']:
            bulletin = Bulletin()
            bulletin.title = request.POST['title']

            if request.POST['text']:
                bulletin.text = request.POST['text']
            elif request.POST['url']:
                if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                    bulletin.url = request.POST['url']

                else:
                    bulletin.url = 'http://' + request.POST['url']
            else:
                bulletin.image = request.FILES['image']
            bulletin.pub_date = timezone.datetime.now()
            bulletin.publisher = request.user
            bulletin.save()

            return redirect('home')
        else:
            return render(request, 'board/create.html', {'error': 'title fields and text, url or image field are required!'})
    else:
        return render(request, 'board/create.html')


def up(request, bulletin_id):
    if request.method == 'POST':
        bulletin = get_object_or_404(Bulletin, pk=bulletin_id)
        bulletin.votes_total += 1
        bulletin.save()
        return redirect('home')
