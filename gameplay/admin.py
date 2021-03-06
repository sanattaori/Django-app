from django.contrib import admin

from .models import Game, Move
# Register your models here.

# Register Game and Move


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_player', 'second_player', 'status')


admin.site.register(Move)