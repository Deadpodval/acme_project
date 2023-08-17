from django.contrib import admin


from .models import Birthday, Tag


@admin.register(Birthday)
class PostAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "birthday"]
    search_fields = ["first_name", "last_name", "birthday"]
    list_filter = ["first_name", "last_name", "birthday"]


@admin.register(Tag)
class PostAdmin(admin.ModelAdmin):
    list_display = ['tag']
    search_fields = ['tag']
    list_filter = ['tag']
