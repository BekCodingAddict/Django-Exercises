# Create your views here.
from django.shortcuts import render
from .models import Room,Topic
from django.contrib.auth.models import User
from .forms import RoomForm
from django.shortcuts import redirect
#rooms=[
#    {'id': 1, 'name': 'Lets learn Python', 'description': 'This is a room for learning Python!'},
#    {'id': 2, 'name': 'Lets learn Django', 'description': 'This is a room for learning Django!'},
#    {'id': 3, 'name': 'Lets learn JavaScript', 'description': 'This is a room for learning JavaScript!'},
#]

def home(request):
    rooms = Room.objects.all()
    topics=Topic.objects.all()
    print("rooms: ", rooms)
    context = {
        'rooms': rooms,
        'topics': topics
    }
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    return render(request, 'base/room.html', {'room': room})

def createRoom(request):
    form=RoomForm()
    if request.method == 'POST':
        print("request.POST: ", request.POST)
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    topics=Topic.objects.all()
    hosts=User.objects.all()
    context={
        'topics': topics,
        'hosts': hosts,
        'form': form
    }

    return render(request, 'base/room_form.html',context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    if request.method == 'POST':
        form=RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    print("form: ", form)
    
    context={
        'form': form
    }
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete_room.html', {'obj': room})