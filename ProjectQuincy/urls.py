from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from static import views as static_views
from search import views as search_views
from people import views as people_views
from communication import views as communication_views 
from places import views as places_views
from activities import views as activities_views

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'ProjectQuincy_views.home', name='home'),
    # url(r'^ProjectQuincy/', include('ProjectQuincy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', static_views.home, name='home'),
    url(r'^about/$', static_views.about, name='about'),
    url(r'^acknowledgements/$', static_views.acknowledgements, name='acknowledgements'),
    url(r'^explore/$', static_views.explore, name='explore'),
    url(r'^visual_essays/$', static_views.visual_essays, name='visual_essays'),
    url(r'^keyword_search/$', search_views.keyword_search, name='keyword_search'),
    url(r'^individuals/$', people_views.individual_list, name='individual_list'),
    url(r'^individuals/(\d+)/$', people_views.individual_detail, name='individual_detail'),
    url(r'^individuals/keyword-search/$', people_views.individual_keyword_search, name='individual_keyword_search'),
    url(r'^letters/$', communication_views.letter_list,name='letter_list'),
    url(r'^locations/$', places_views.location_list, name='location_list'),
    url(r'^locations/(\d+)/$', places_views.location_detail, name='location_detail'),
    url(r'^locations/keyword-search/$', places_views.location_keyword_search, name='location_keyword_search'),
    url(r'^location_tree.json$', places_views.location_tree),
    url(r'^location_circlepack/$', places_views.location_circlepack, name="location_circlepack"),
    url(r'^location_dendrogram/$', places_views.location_dendrogram, name="location_dendrogram"),
    url(r'^regions/$', places_views.region_list, name='region_list'),
    url(r'^regions/(\d+)/$', places_views.region_detail, name='region_detail'),
    url(r'^continents/$', places_views.continent_list, name='continent_list'),
    url(r'^continents/(\d+)/$', places_views.continent_detail, name='continent_detail'),
    url(r'^states/$', places_views.state_list, name='state_list'),
    url(r'^states/(\d+)/$', places_views.state_detail, name='state_detail'),
    url(r'^assignment_types/$', activities_views.assignment_type_list, name='assignment_type_list'),
    url(r'^assignment_types/(\d+)/$', activities_views.assignment_type_detail, name='assignment_type_detail'),
    url(r'^assignment_titles/$', activities_views.assignment_title_list, name='assignment_title_list'),
    url(r'^assignment_titles/(\d+)/$', activities_views.assignment_title_detail, name='assignment_title_detail'),
    url(r'^assignment_titles/keyword_search/$', activities_views.assignment_title_keyword_search, name='assignment_title_keyword_search'),
    url(r'^assignment_sunburst/$', activities_views.assignment_sunburst, name='assignment_sunburst'),
    url(r'^assignment_bubble/$', activities_views.assignment_bubble, name='assignment_bubble'),
    url(r'^assignment_by_type.json$', activities_views.assignment_by_type),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls)
    ]
