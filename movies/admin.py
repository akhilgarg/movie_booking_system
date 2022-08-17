from django.contrib import admin

# Register your models here.
from movies.models import Movie, Theatre, Screen, Show


class MovieAdmin(admin.ModelAdmin):
    pass


class TheatreAdmin(admin.ModelAdmin):
    pass


class ScreenAdmin(admin.ModelAdmin):
    pass


class ShowAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)
admin.site.register(Theatre, TheatreAdmin)
admin.site.register(Screen, ScreenAdmin)
admin.site.register(Show, ShowAdmin)
