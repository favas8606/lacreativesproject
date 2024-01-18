
# Create your views here.
from django.shortcuts import render
from . models import Message
import time

# Create your views here.
def index(request):

    try:
        time.sleep(2)

        if request.method == 'POST':
            name = request.POST['name']
            phonenumber = request.POST['phonenumber']
            email = request.POST['email']
            message = request.POST['message']

            if len(phonenumber) < 10 or name is None or email is None or message is None :
                 return render(request, 'index.html')
            else:
                register = Message(name=name, phonenumber=phonenumber,email=email,messages=message)
                if register is not None:
                    register.save()

           

    except:
        print('Error occured')
            


    return render(request,'index.html')


 