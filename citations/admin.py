#This file activates and customizes django's built-in admin interface for the CITATIONS app

#At some point I need to figure out how to attach Validation records to linking tables.
#Hopefully a patch for nested inlines will be completed soon...

from citations.models import Bibliography, Citation

from django.contrib import admin

admin.site.register(Bibliography)

class CitationAdmin(admin.ModelAdmin):
	fields = ('title', 'bibliography', ('pages', 'canonic_url'), 'notes')
	search_fields = ('title', 'bibliography__entry', 'notes')
admin.site.register(Citation, CitationAdmin)