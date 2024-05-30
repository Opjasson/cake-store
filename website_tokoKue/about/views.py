from django.shortcuts import render

def index(request):
    context = {
        'nav':[
            ['/about','Home'],
            ['donuts/','Donuts'],
            ['cake/','Cake'],
            ['pastry/','Pastry']
        ]
        
    }
    
    return render(request,'about.html',context)
