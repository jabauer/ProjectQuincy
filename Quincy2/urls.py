from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Quincy2.views.home', name='home'),
    # url(r'^Quincy2/', include('Quincy2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', 'static.views.home', name='home'),
    url(r'^about/$', 'static.views.about', name='about'),
    url(r'^acknowledgements/$', 'static.views.acknowledgements', name='acknowledgements'),
    url(r'^explore/$', 'static.views.explore', name='explore'),
    url(r'^keyword_search/$', 'search.views.keyword_search', name='keyword_search'),
    url(r'^individuals/$', 'people.views.individual_list', name='individual_list'),
    url(r'^individuals/(\d+)/$', 'people.views.individual_detail', name='individual_detail'),
    url(r'^individuals/keyword-search/$', 'people.views.individual_keyword_search', name='individual_keyword_search'),
    url(r'^letters/$', 'communication.views.letter_list',name='letter_list'),
	url(r'^locations/$', 'places.views.location_list', name='location_list'),
	url(r'^locations/(\d+)/$', 'places.views.location_detail', name='location_detail'),
	url(r'^locations/keyword-search/$', 'places.views.location_keyword_search', name='location_keyword_search'),
    url(r'^location_tree.json$', 'places.views.location_tree'),
    url(r'^location_circlepack/$', 'places.views.location_circlepack', name="location_circlepack"),
    url(r'^location_dendrogram/$', 'places.views.location_dendrogram', name="location_dendrogram"),
	url(r'^regions/$', 'places.views.region_list', name='region_list'),
	url(r'^regions/(\d+)/$', 'places.views.region_detail', name='region_detail'),
	url(r'^continents/$', 'places.views.continent_list', name='continent_list'),
	url(r'^continents/(\d+)/$', 'places.views.continent_detail', name='continent_detail'),
	url(r'^states/$', 'places.views.state_list', name='state_list'),
	url(r'^states/(\d+)/$', 'places.views.state_detail', name='state_detail'),
	url(r'^assignment_types/$', 'activities.views.assignment_type_list', name='assignment_type_list'),
	url(r'^assignment_types/(\d+)/$', 'activities.views.assignment_type_detail', name='assignment_type_detail'),
	url(r'^assignment_titles/$', 'activities.views.assignment_title_list', name='assignment_title_list'),
	url(r'^assignment_titles/(\d+)/$', 'activities.views.assignment_title_detail', name='assignment_title_detail'),
    url(r'^assignment_titles/keyword_search/$', 'activities.views.assignment_title_keyword_search', name='assignment_title_keyword_search'),
    url(r'^assignment_sunburst/$', 'activities.views.assignment_sunburst', name='assignment_sunburst'),
    url(r'^assignment_bubble/$', 'activities.views.assignment_bubble', name='assignment_bubble'),
    url(r'^assignment_by_type.json$', 'activities.views.assignment_by_type'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
