from django.shortcuts import render
from datetime import datetime

from module.models import location_statistics


def dashboard(request):

    now = datetime.now() 
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")



    context = { 
                'quantity' : 1000,
                'speedover' : 200,
                'average_speed' :  120
    }
                	

    return render(request, 'index.html', context)







