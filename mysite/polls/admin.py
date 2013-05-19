from django.contrib import admin
from polls.models import Poll, Choice
from django import forms
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_recently')
    fieldsets = [
            ('Question',         {'fields':['question']}),
            ('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
            ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

class ChoiceForm(forms.ModelForm):
    email = forms.EmailField(initial='dingman@gmail.com')
    class Meta:
        model = Choice

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        # instance is obj here
        if instance:
            self.base_fields['email'].initial = 'dingman@gmai.com'
        else:
            self.base_fields['email'].initial = ''
        forms.ModelForm.__init__(self, *args, **kwargs)    

class ChoiceAdmin(admin.ModelAdmin):
    form = ChoiceForm

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
