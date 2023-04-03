from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import *
import admin_interface

# Register your models here.
admin.site.site_header="CETUS Interior Products"
admin.site.index_title="Dashboard"

admin.site.unregister(User)
admin.site.unregister(Group)



admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(brochure)
admin.site.register(Requirnment)
admin.site.register(Register)
admin.site.register(newsletter)
admin.site.register(image)