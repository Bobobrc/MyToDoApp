from django.contrib import admin
from todoapp.models import List, Task

# Register your models here.
admin.site.register(List)
admin.site.register(Task)