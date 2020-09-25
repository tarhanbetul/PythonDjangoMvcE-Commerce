from django.contrib import admin

# Register your models here.


from .models import Question
from .models import Choice

admin.site.site_header="Test Admin"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets =[
        ('soru bilgisi', {'fields':['question_text']}),
        ('tarih bilgisi', {'fields':['pub_date'],'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)