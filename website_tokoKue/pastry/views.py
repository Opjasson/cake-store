from django.shortcuts import render

def index(request):
    context = {
        'nav' : [
            ['/','Home'],
            ['donuts/','Donuts'],
            ['cake/','Cake'],
            ['pastry/','Pastry']
        ]
    }
    return render(request,"pastry.html",context)