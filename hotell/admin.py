from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Hotel

# Register your models here.

from django.contrib import admin
from .models import Hotel

admin.site.register(Hotel)
admin.site.unregister(User)
admin.site.unregister(Group)
