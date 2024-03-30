from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Import models
from .models import MerchType
from .models import Artist
from .models import Group
from .models import Merch

# Create views
# Listview
class MerchTypeList(ListView):
    model = MerchType
    context_object_name = 'MerchTypeList'
    template_name = 'Articles/MerchTypeList.html'

class ArtistList(ListView):
    model = Artist
    context_object_name = 'ArtistList'
    template_name = 'Articles/ArtistList.html'

class GroupList(ListView):
    model = Group
    context_object_name = 'GroupList'
    template_name = 'Articles/GroupList.html'

class MerchList(ListView):
    model = Merch
    context_object_name = 'MerchList'
    template_name = 'Articles/MerchList.html'