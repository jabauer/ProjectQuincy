#This file activates and customizes the django admin inferface for the PLACES app

from django.contrib import admin

from citations.models import Validation
from django.contrib.contenttypes import generic

class ValidationInline(generic.GenericStackedInline):
	model = Validation
	extra = 0

from places.models import Location, CoordinateSystem, State, InState, Region, InRegion, Empire, InEmpire

class InStateInline(admin.TabularInline):
	model = InState
	inlines = [ValidationInline]
	extra = 0

class InRegionInline(admin.TabularInline):
	model = InRegion
	extra = 0

class InEmpireInline(admin.TabularInline):
	model = InEmpire
	extra = 0

class LocationAdmin(admin.ModelAdmin):
	fields = ('name', ('lat', 'long', 'coordinate_system'), 'notes')
	inlines = [InStateInline, InRegionInline, ValidationInline]
	search_fields = ['name', 'notes']
admin.site.register(Location, LocationAdmin)

class CoordinateSystemAdmin(admin.ModelAdmin):
	pass
admin.site.register(CoordinateSystem, CoordinateSystemAdmin)

class StateAdmin(admin.ModelAdmin):
	inlines = [InStateInline, InEmpireInline]
	search_fields = ['name', 'notes']
	ordering = ('name',)
admin.site.register(State, StateAdmin)

class RegionAdmin(admin.ModelAdmin):
	inlines = [InRegionInline]
admin.site.register(Region, RegionAdmin)

class EmpireAdmin(admin.ModelAdmin):
	inlines = [InEmpireInline]
admin.site.register(Empire, EmpireAdmin)