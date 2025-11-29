# Create your views here.
from django.shortcuts import render

rooms=[
    {'id': 1, 'name': 'Lets learn Python', 'description': 'This is a room for learning Python!'},
    {'id': 2, 'name': 'Lets learn Django', 'description': 'This is a room for learning Django!'},
    {'id': 3, 'name': 'Lets learn JavaScript', 'description': 'This is a room for learning JavaScript!'},
]

def home(request):
    context = {
        'rooms': rooms
    }
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for r in rooms:
        if r['id'] == int(pk):
            room = r
            break
    context = {
        'room': room
    }
    return render(request, 'base/room.html', context)
