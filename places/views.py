#places/views.py
#This files contains the view functions for the PLACES APP.

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from simplesearch.functions import *

from .models import Continent, State, Location, Region, InRegion, InState
from activities.models import Assignment
from citations.models import Validation

import operator

def continent_list(request):
	return render(request, 'places/continent_list.html', {'continents': Continent.objects.all().order_by('name')})

def continent_detail(request, continent_id):
	continent = get_object_or_404(Continent, id=continent_id)
	states = State.objects.filter(continent_id=continent_id).order_by('name')
	dictionary = {'continent': continent,
		'states': states}
	return render(request, 'places/continent_detail.html', dictionary)

def state_list(request):
	return render(request, 'places/state_list.html', {'states': State.objects.all().order_by('name')})

def state_detail(request, state_id):
	state = get_object_or_404(State, id=state_id)
	in_states = InState.objects.filter(state_id=state_id)
	dictionary = {'state': state, 'in_states':in_states}
	return render(request, 'places/state_detail.html', dictionary)

def location_list(request):
	return render(request, 'places/location_list.html', {'locations': Location.objects.all().order_by('name')})

def location_detail(request, location_id):
	location = get_object_or_404(Location, id=location_id)
	in_regions = InRegion.objects.filter(location_id=location_id)
	in_states = InState.objects.filter(location_id=location_id)
	footnotes = Validation.objects.all()
	dictionary = {'location': location, 'footnotes':footnotes, 'in_regions': in_regions, 'in_states':in_states}
	return render(request, 'places/location_detail.html', dictionary)

def location_keyword_search(request):
	if 'q' in request.GET:
		query_string = request.GET['q']
		entry_query = get_query(query_string, ['name', 'notes'])
		locations = Location.objects.filter(entry_query).distinct().order_by("name")
	dictionary = {'query_string': query_string, 'locations':locations}
	return render(request, 'places/location_keyword_search.html', dictionary)

def region_list(request):
	return render(request, 'places/region_list.html', {'regions': Region.objects.all().order_by('name')})

def region_detail(request, region_id):
	region = get_object_or_404(Region, id=region_id)
	in_regions = InRegion.objects.filter(region_id=region_id)
	dictionary = {'region': region, 'in_regions':in_regions}
	return render(request, 'places/region_detail.html', dictionary)

def location_tree(request):
	return_dict = {'name': 'locations', 'level':'locations', 'id':'', 'children': []}
	continent_list = []
	for c in Continent.objects.all():
		continent_list.append({'name': c.name, 'level': 'continents', 'id': c.id, 'children': []})
	for cl in continent_list:
		cont_id = cl['id']
		state_objects = State.objects.filter(continent=cont_id)
		for so in state_objects:
			state_dict = {}
			state_dict['name'] = so.name
			state_dict['level'] = 'states'
			state_dict['id'] = so.id
			state_dict['children'] = []

			in_state_objects = InState.objects.filter(state=so.id)
			for i_s in in_state_objects:
				location_object = i_s.location
				location_dict = {}
				location_dict['name'] = location_object.name
				location_dict['id'] = location_object.id
				location_dict['level'] = 'locations'
				assignments = Assignment.objects.filter(location=location_object.id)
				for a in assignments:
					total_years = 0
					if a.start_year is not None and a.end_year is not None:
						full_years = int(a.end_year) - int(a.start_year)
						total_years += full_years
						location_dict['total_years'] = total_years
				location_dict['size'] = assignments.count()
				state_dict['children'].append(location_dict)
			cl['children'].append(state_dict)

	return_dict['children'] = continent_list
	import json
	jstring = json.dumps(return_dict, sort_keys=True, indent=2)
	return HttpResponse(jstring, content_type=u'text/javascript; charset=utf8')

def location_circlepack(request):
	return render(request, 'places/location_circlepack.html')

def location_dendrogram(request):
	return render(request, 'places/location_dendrogram.html')





