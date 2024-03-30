from django.contrib import admin
from . models import MerchType, Artist, Group, Merch

# Register your models here.
admin.site.register(MerchType)
admin.site.register(Artist)
admin.site.register(Group)
admin.site.register(Merch)