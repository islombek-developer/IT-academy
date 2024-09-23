from django.contrib import admin
from .models import Lesson,Homework,Davomat,Date,Homework_file

class LikeInline(admin.StackedInline):
    model=Homework_file
    extra=1


@admin.register(Homework)
class AdminLesson(admin.ModelAdmin):
    list_display = ('student', 'team')
    list_display_links = ('student',)
    list_editable = ('team',)
    list_filter = ('team',)
    inlines = [
        LikeInline
    ]


admin.site.register(Lesson)
admin.site.register(Davomat)
admin.site.register(Date)
