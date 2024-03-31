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
    context_object_name = 'MerchType'
    template_name = 'Articles/MerchTypeList.html'

class ArtistList(ListView):
    model = Artist
    context_object_name = 'Artist'
    template_name = 'Articles/ArtistList.html'

    def get_queryset(self):
        return Artist.objects.prefetch_related('group_set')

class GroupList(ListView):
    model = Group
    context_object_name = 'Group'
    template_name = 'Articles/GroupList.html'

class MerchList(ListView):
    model = Merch
    context_object_name = 'Merch'
    template_name = 'Articles/MerchList.html'

# Createview

class MerchTypeCreate(CreateView):
    model = MerchType
    context_object_name = 'MerchType'
    fields = '__all__'
    template_name = 'Articles/MerchTypeForm.html'

class ArtistCreate(CreateView):
    model = Artist
    context_object_name = 'Artist'
    fields = '__all__'
    template_name = 'Articles/ArtistForm.html'
    success_url = reverse_lazy('ArtistList')


class GroupCreate(CreateView):
    model = Group
    context_object_name = 'Group'
    fields = '__all__'
    template_name = 'Articles/GroupForm.html'
    success_url = reverse_lazy('GroupList')

class MerchCreate(CreateView):
    model = Merch
    context_object_name = 'Merch'
    fields = '__all__'
    template_name = 'Articles/MerchForm.html'

#Update view
    
class MerchTypeUpdate(UpdateView):
    model = MerchType
    fields = '__all__'
    template_name = 'Articles/MerchTypeForm.html'

class ArtistUpdate(UpdateView):
    model = Artist
    fields = '__all__'
    template_name = 'Articles/ArtistForm.html'
    success_url = reverse_lazy('ArtistList')

class GroupUpdate(UpdateView):
    model = Group
    fields = '__all__'
    template_name = 'Articles/GroupForm.html'
    success_url = reverse_lazy('GroupList')

class MerchUpdate(UpdateView):
    model = Merch
    fields = '__all__'
    template_name = 'Articles/MerchForm.html'

#Delete view
class MerchTypeDelete(DeleteView):
    model = MerchType
    context_object_name = 'MerchType'
    template_name = 'Articles/MerchTypeDelete.html'
    success_url = reverse_lazy('')

class ArtistDelete(DeleteView):
    model = Artist
    context_object_name = 'Artist'
    template_name = 'Articles/ArtistDelete.html'
    success_url = reverse_lazy('ArtistList')

class GroupDelete(DeleteView):
    model = Group
    context_object_name = 'Group'
    template_name = 'Articles/GroupDelete.html'
    success_url = reverse_lazy('GroupList')


class MerchDelete(DeleteView):
    model = Merch
    context_object_name = 'Merch'
    template_name = 'Articles/MerchDelete.html'
    success_url = reverse_lazy('')