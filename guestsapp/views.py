from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from .models import Guest
from django.core.exceptions import ObjectDoesNotExist
from .forms import GuestForm


# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the guests app")


# Will show all users in the table
def listUsers(request):
    guests = Guest.get_all_users()
    return render(request, 'list-users.html', {"guests": guests})


def getGuest(request, id):
    try:
        modelguest = Guest.get_oneUser(id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,'show-guest.html',{"modelguest":modelguest})


def guestForm(request):
    #dictionary to store initial data, we will use field names as keys
    context = {}
    lastGuest = Guest.objects.all().last()
    lastGuestid = lastGuest.id
    newGuestid = lastGuestid+1

    form = GuestForm(request.POST or None)
    if form.is_valid():        
        my_form = form.save(commit=False);
        my_form.id = newGuestid
        my_form.save()
        return redirect('listusers')


    context['form'] = form
    return render(request,"create-guest.html", context)

    
def updateGuest(request, id):
    guest = Guest.get_oneUser(id)
    form = GuestForm(initial={
        'first_name':guest.first_name,
        'last_name':guest.last_name,
        'email':guest.email,
        'id_number':guest.id_number,
        'gender':guest.gender        
        })
    if request.method == "POST":
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('showguest', id=id)
            except Exception as e:
                pass
    return render(request,'update-guest.html',{'form':form,'guest':guest})


def deleteGuest(request, id):
    guest = Guest.get_oneUser(id)
    try:
        guest.delete()
    except:
        pass
    return redirect('listusers')