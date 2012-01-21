from kanji.models import Kanji, Onyomi, Kunyomi, Meaning, Nanori, Definition
from django.contrib import admin

class KanjiAdmin(admin.ModelAdmin):
    list_display = ['literal', 'stroke_count', 'grade']
    list_filter = ['stroke_count', 'grade']
    search_fields = ['literal']

admin.site.register(Kanji, KanjiAdmin)
admin.site.register(Onyomi)
admin.site.register(Kunyomi)
admin.site.register(Meaning)
admin.site.register(Nanori)
admin.site.register(Definition)
