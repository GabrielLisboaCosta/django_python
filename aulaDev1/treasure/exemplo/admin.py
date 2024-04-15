from django.contrib import admin
from exemplo.models import Example
from exemplo.models import Passaport
from exemplo.models import Person

# Register your models here.
admin.site.register(Example)
admin.site.register(Passaport)
admin.site.register(Person)
