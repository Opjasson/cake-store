from django.shortcuts import render


def index(request):
    context = {
        'nav' : [
            ['/','Home'],
            ['/about/donuts','Donuts'],
            ['/about/cake','Cake'],
            ['/about/pastry','Pastry']
        ]
    }
    
    return render(request,"donuts.html",context)