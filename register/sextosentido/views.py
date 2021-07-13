from django.shortcuts import render
from .models import Item, Consumer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def register(request, sku):
    #register with sku in url

    items = Item.objects.all()
    
    if request.method == 'POST':
       
        print(request.POST)
        registeredSku = request.POST.get('inputSku',"")
        email = request.POST.get('email',"")
        username = email 
       
        password = request.POST.get('inputPassword',"")
        first_name = request.POST.get('first_name',"")
        last_name = request.POST.get('last_name',"")
        country = request.POST.get('country',"country")
        city = request.POST.get('city', "city")
        where = request.POST.get('where', 'where')
        when = request.POST.get('when', 'when')
        telephone = request.POST.get('telephone', '')
        getInfo = request.POST.get('getInfo', 'Off')
        
        if getInfo == 'on':
            getInfo = True
        else:
            getInfo = False
        #item must exist in db
        item=items.get(sku=registeredSku)
        
        #if user does not exist, create new user, if user exist, request login, if session authenticated, continue
        if request.user.is_authenticated:
            user = request.user
            pass
        else:
            user = User.objects.create_user(username,email,password)
            user.first_name = first_name
            user.last_name = last_name
            user.email_address = email
            user.save()

        #create consumer registration
        newConsumer = Consumer(user_id=user,sku=item, where=where,when=when,country=country,city=city,getInfo=getInfo )
        newConsumer.save()

        #inform user everything saved ok and direct to profile to view registered products

        

    return render(request, 'sextosentido/registration.html', {'sku': sku})





