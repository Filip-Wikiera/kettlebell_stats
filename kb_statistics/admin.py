from django.contrib import admin

from django.contrib import admin
from .models import Exercise, Session
from django.contrib.auth.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', "is_staff")
    list_filter = ('is_staff', 'is_superuser')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "type")


admin.site.register(Exercise, ExerciseAdmin)


class SessionAdmin(admin.ModelAdmin):
    list_display = ("exercise", "rep_count", "weight", "person", "date")


admin.site.register(Session, SessionAdmin)
