from django.urls import path
from .views import MerchTypeList, MerchTypeCreate, MerchTypeUpdate, MerchTypeDelete
from .views import ArtistList, ArtistCreate, ArtistUpdate, ArtistDelete
from .views import GroupList, GroupCreate, GroupUpdate, GroupDelete
from .views import MerchList, MerchCreate, MerchUpdate, MerchDelete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    #MerchType URLs
    path('MerchTypeList/', MerchTypeList.as_view(), name = 'MerchTypeList'),
    path('MerchTypeCreate/', MerchTypeCreate.as_view(), name = 'MerchTypeCreate'),
    path('MerchTypeUpdate/<int:pk>/', MerchTypeUpdate.as_view(), name = 'MerchTypeUpdate'),
    path('MerchTypeDelete/<int:pk>/', MerchTypeDelete.as_view(), name = 'MerchTypeDelete'),

    #Artist URLs
    path('ArtistList/', ArtistList.as_view(), name = 'ArtistList'),
    path('ArtistCreate/', ArtistCreate.as_view(), name = 'ArtistCreate'),
    path('ArtistUpdate/<int:pk>/', ArtistUpdate.as_view(), name = 'ArtistUpdate'),
    path('ArtistDelete/<int:pk>/', ArtistDelete.as_view(), name = 'ArtistDelete'),

    #Group URLs
    path('GroupList/', GroupList.as_view(), name = 'GroupList'),
    path('GroupCreate/', GroupCreate.as_view(), name = 'GroupCreate'),
    path('GroupUpdate/<int:pk>/', GroupUpdate.as_view(), name = 'GroupUpdate'),
    path('GroupDelete/<int:pk>/', GroupDelete.as_view(), name = 'GroupDelete'),

    #Merch URLs
    path('MerchList/', MerchList.as_view(), name = 'MerchList'),
    path('MerchCreate/', MerchCreate.as_view(), name = 'MerchCreate'),
    path('MerchUpdate/<int:pk>/', MerchUpdate.as_view(), name = 'MerchUpdate'),
    path('MerchDelete/<int:pk>/', MerchDelete.as_view(), name = 'MerchDelete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)