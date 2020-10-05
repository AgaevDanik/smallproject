from .models import *
from django.contrib import admin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'gender', 'phone_number')
    list_editable = ('full_name', 'email', 'gender', 'phone_number')
    search_fields = ('full_name', 'email', 'phone_number', )
    readonly_fields = ('id',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'fees', )
    list_editable = ('name', 'description',)
    search_fields = ('name', )
    readonly_fields = ('id', )


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'language_name')
    readonly_fields = ('id', )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'events_name', 'events_date_start', 'events_date_end')
    readonly_fields = ('id', )

