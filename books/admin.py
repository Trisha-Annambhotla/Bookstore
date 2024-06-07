from django.contrib import admin
from .models import Book

# Register your models here.
# admin.site.register(Book)

# In order to display the data in more reader friendly manner

class BookAdmin(admin.ModelAdmin):
    list_display = ('Title','Author','Genre')

admin.site.register(Book,BookAdmin)
