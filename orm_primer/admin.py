from django.contrib import admin

# Register your models here.
# из файла models импортируем модель Post
from .models import Post, Operator, Station, Work_in_station


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    # это свойство сработает для всех колонок: где пусто - там будет эта строка
    empty_value_display = "-пусто-"



# при регистрации модели Post источником конфигурации для неё назначаем класс PostAdmin
admin.site.register(Post, PostAdmin)
admin.site.register(Operator)
admin.site.register(Station)
admin.site.register(Work_in_station)
