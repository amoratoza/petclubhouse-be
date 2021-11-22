from django.contrib import admin

from .models.user import User
from .models.pet import Pet
from .models.booking import Booking

admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Booking)
