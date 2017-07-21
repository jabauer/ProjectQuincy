##This file contains the view functions for the PEOPLE App

from django.shortcuts import render, redirect, get_object_or_404
from simplesearch.functions import *
from .models import Individual

#to enable footnotes
from citations.models import Validation
from django.contrib.contenttypes.models import ContentType

import operator
from utility_code import partial_date

def individual_list(request):
	return render(request, 'people/individual_list.html', {'individuals': Individual.objects.all().order_by("sort_name")})

def individual_detail(request, individual_id):
	individual = get_object_or_404(Individual, id=individual_id)
	footnotes = Validation.objects.all()
	birth_date = partial_date(individual.birth_date, individual.birth_year_known, individual.birth_month_known, individual.birth_day_known)
	death_date = partial_date(individual.death_date, individual.death_year_known, individual.death_month_known, individual.death_day_known)
	dictionary = {'individual': individual, 'footnotes': footnotes, 'birth_date': birth_date, 'death_date':death_date}
	return render(request, 'people/individual_detail.html', dictionary)

def individual_keyword_search(request):
	if 'q' in request.GET:
		query_string = request.GET['q']
		entry_query = get_query(query_string, ['name', 'notes'])
		individuals = Individual.objects.filter(entry_query).distinct().order_by("sort_name")
	dictionary = {'query_string': query_string, 'individuals':individuals}
	return render(request, 'people/individual_keyword_search.html', dictionary)