from django.contrib import admin
from exemplo.models import Example
from exemplo.models import Passaport
from exemplo.models import Person
from exemplo.models import Reporter
from exemplo.models import Article
from exemplo.models import Magazine

# Register your models here.
admin.site.register(Example)
admin.site.register(Passaport)
admin.site.register(Person)
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Magazine)

