from django.contrib import admin

from .models import BlogNote


@admin.register(BlogNote)
class BlogNoteAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
