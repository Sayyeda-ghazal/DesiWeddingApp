from django.contrib import admin
from planner.models import EventType, Menu, QuoteRequest

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display  = ('id', 'name', 'description')
    search_fields = ('name',)

    def __str__(self):
        return self.name

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_per_guest')
    search_fields = ('name',)
    list_filter = ('categories',) 
    readonly_fields = ('id',)



@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'event_type', 'menu', 'guests', 'created_at')
    search_fields = ('name', 'email', 'phone')  
    list_filter = ('event_type', 'menu', 'created_at')  
    readonly_fields = ('created_at',)