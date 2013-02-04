#This file activates and customizes django's default admin interfact for the PEOPLE app

#Will have to add support for Relationships and Residences later on -- will be inline for IndividualAdmin

from django.contrib import admin
from people.models import Individual, RelationshipType, OccupationType, OccupationTitle, ResidenceType, Occupation, Relationship
from activities.models import Assignment

class AssignmentInline(admin.StackedInline):
	model = Assignment
	extra = 0
	ordering = ('assignment_title',)

class OccupationInline(admin.StackedInline):
	model = Occupation
	extra = 0
	ordering = ('occupation_title',)

from citations.models import Validation
from django.contrib.contenttypes import generic

class ValidationInline(generic.GenericStackedInline):
	model = Validation
	extra = 0
	ordering = ('citation',)

class IndividualAdmin(admin.ModelAdmin):
	fields = ('id', ('name', 'sort_name'), 'sex', 'american', ('birth_date', 'birth_year_known', 'birth_month_known', 'birth_day_known'), ('death_date', 'death_year_known', 'death_month_known', 'death_day_known'), 'state', 'notes', ('created_at', 'updated_at'))
	inlines = (OccupationInline, AssignmentInline, ValidationInline,)
	search_fields = ['name', 'sex', 'notes']
	list_display = ('name',)
	readonly_fields = ['id', 'created_at', 'updated_at']
	ordering = ('sort_name',)
admin.site.register(Individual, IndividualAdmin)


class RelationshipTypeAdmin(admin.ModelAdmin):
	pass
admin.site.register(RelationshipType, RelationshipTypeAdmin)

class OccupationTypeAdmin(admin.ModelAdmin):
	ordering = ('name',)
admin.site.register(OccupationType, OccupationTypeAdmin)


class OccupationTitleAdmin(admin.ModelAdmin):
	ordering = ('name',)
admin.site.register(OccupationTitle, OccupationTitleAdmin)


class ResidenceTypeAdmin(admin.ModelAdmin):
	pass
admin.site.register(ResidenceType, ResidenceTypeAdmin)
