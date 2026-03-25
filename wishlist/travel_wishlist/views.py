from django.shortcuts import render

# Create your views here.

def place_list(request):
    return render(request, 'travel_wishlist/wishlist.html')