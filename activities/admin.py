#This file activates and customizes the backend admin site for the ACTIVITIES app.

from django.contrib import admin
from activities.models import Assignment, AssignmentTitle, AssignmentType

from citations.models import Validation
from django.contrib.contenttypes.admin import GenericStackedInline

class ValidationInline(GenericStackedInline):

	model = Validation
	extra = 0

class AssignmentAdmin(admin.ModelAdmin):
	fields = ('id', 'individual', 'assignment_title', 'location', ('start_year', 'start_certain'), ('end_year', 'end_certain'), 'notes')
	inlines = [ValidationInline]
	search_fields = ['individual__name', 'assignment_title__name', 'location__name', 'notes']
	list_display = ('individual', 'assignment_title', 'location', 'start_year', 'end_year')
	readonly_fields = ['id']
	ordering = ('start_year', 'end_year',)
admin.site.register(Assignment, AssignmentAdmin)

class AssignmentTitleAdmin(admin.ModelAdmin):
	search_fields = ['name', 'notes']
	readonly_fields = ['id']
	list_display = ('name', 'assignment_type')
	ordering = ('name',)
admin.site.register(AssignmentTitle, AssignmentTitleAdmin)

class AssignmentTypeAdmin(admin.ModelAdmin):
	ordering = ('name',)
admin.site.register(AssignmentType)