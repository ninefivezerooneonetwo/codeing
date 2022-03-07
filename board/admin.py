from django.contrib import admin

# Register your models here.
from board.models import Info


class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'pub_date');
admin.site.register(Info, InfoAdmin)