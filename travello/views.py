from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.name = 'Visakapatnam'
    dest1.desc = 'The city of Destination'
    dest1.img = 'destination_1.jpg'
    dest1.price = 760
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'First Biryani, Then Sherwani'
    dest2.img = 'destination_2.jpg'
    dest2.price = 650
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Bangaluru'
    dest3.desc = 'Beautiful city'
    dest3.img = 'destination_3.jpg'
    dest3.price = '760'
    dest3.offer = True

    dests = [dest1, dest2, dest3]

    return render(request, "index.html", {'dests': dests})
