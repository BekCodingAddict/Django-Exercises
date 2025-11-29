from django.contrib import admin

# Register your models here.
from .models import Room,Topic,Message


#class RoomAdmin(admin.ModelAdmin):
#	list_display=('id', 'name', 'description', 'host', 'topic')
#	search_fields=('name', 'description')
#	list_filter=('name', 'description')
#	list_editable=('description',)


admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)