from django.shortcuts import render
from .models import  Wishlist, mysavereel
from random import randint
# Create your views here.

def home(request):
    if request.method == 'POST':
        img_path=request.POST['img_path']
        original_price=randint(100, 1000)
        Wishlist.objects.create(
            name="Prodict "+str(randint(0, 100)),
            description="This is random description",
            original_price=original_price,
            discounted_price= original_price- randint(10, 100),
            offer=randint(1, 5),
            image_path=img_path
        )
        wishlist_data = Wishlist.objects.all()
        
        return render(request, 'home.html', {'wishlist_data': wishlist_data})
    return render(request, 'home.html')

def explore(request):
    return render(request, 'explore.html')

def profile(request):   
    wishlist=Wishlist.objects.all()
    if request.method == 'POST':
        id=request.POST['id']
        Wishlist.objects.filter(id=id).delete()
        wishlist=Wishlist.objects.all()
    if wishlist:
        return render(request, 'profile.html', {'wishlist': wishlist})
    return render(request, 'profile.html')


def mysaved(request):
    reels=mysavereel.objects.all()
    if request.method == 'POST':
        id=request.POST['id']
        mysavereel.objects.filter(id=id).delete()
        reels=mysavereel.objects.all()
    if reels:
        return render(request, 'mysaved.html', {'reels': reels})
    return render(request, 'mysaved.html')


def chat(request):
    return render(request, 'chat.html')

def reel(request):
    if request.method == 'POST':
        reel_path=request.POST['reel_path']
        mysavereel.objects.create(
            path=reel_path
        )
        return render(request, 'reel.html')
    return render(request, 'reel.html')