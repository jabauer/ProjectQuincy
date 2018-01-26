#This file activates and customizes the django admin interface for the
#COMMUNICATION app

from django.contrib import admin 
from django.contrib.contenttypes.admin import GenericStackedInline

from communication.models import Letter, Enclosure
from citations.models import Validation

class EnclosureInline(admin.TabularInline):
	model = Enclosure
	fk_name = 'main_letter'
	readonly_fields = ['id']
	extra = 1

class ValidationInline(GenericStackedInline):
	model = Validation
	extra = 0

class LetterAdmin(admin.ModelAdmin):     
	fields = ('id', 'title', ('from_individual', 'from_organization'), ('to_individual', 'to_organization'), 'from_location', 'to_location', 'circular', ('date_sent', 'sent_year_known', 'sent_month_known', 'sent_day_known'), ('date_received', 'received_year_known', 'received_month_known', 'received_day_known'), ('date_docketed', 'docketed_year_known', 'docketed_month_known', 'docketed_day_known'), 'notes')
	inlines = [EnclosureInline, ValidationInline]
	search_fields = ['title', 'to_location__name', 'notes']
	readonly_fields = ['id']

admin.site.register(Letter, LetterAdmin)