from article.models import *
from django.contrib import admin


class CommentsInLine(admin.StackedInline):
    model = Comments
    extra = 2


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'creation_date', 'was_published_recently')
    fieldsets = [(None, {'fields': ['title', 'subtitle', 'text']}),
                 ('Додаткова інформація', {'fields': ['url', 'type']}),
                 ('Створено:', {'fields': ['author', ]})]
    inlines = [CommentsInLine]
    list_filter = ['title', 'creation_date', 'author']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Comments)

