# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import AssignmentType, AssignmentTitle, Assignment
from citations.models import Validation
from simplesearch.functions import *
from django.http import HttpResponse

def assignment_type_list(request):
	return render(request, 'activities/assignment_type_list.html', {'assignment_types': AssignmentType.objects.all()})

def assignment_type_detail(request, assignment_type_id):
	assignment_type = get_object_or_404(AssignmentType, id=assignment_type_id)
	assignment_titles = AssignmentTitle.objects.filter(assignment_type_id=assignment_type_id)
	dictionary = {'assignment_type': assignment_type,
		'assignment_titles': assignment_titles}
	return render(request, 'activities/assignment_type_detail.html', dictionary)

def assignment_title_list(request):
	return render(request, 'activities/assignment_title_list.html', {'assignment_titles': AssignmentTitle.objects.all()})

def assignment_title_detail(request, assignment_title_id):
	assignment_title = get_object_or_404(AssignmentTitle, id=assignment_title_id)
	footnotes = Validation.objects.all()
	dictionary = {'assignment_title': assignment_title,
		'footnotes': footnotes}
	return render(request, 'activities/assignment_title_detail.html', dictionary)

def assignment_title_keyword_search(request):
	if 'q' in request.GET:
		query_string = request.GET['q']
		entry_query = get_query(query_string, ['name', 'notes'])
		assignment_titles = AssignmentTitle.objects.filter(entry_query).distinct().order_by("name")
	dictionary = {'query_string': query_string, 'assignment_titles':assignment_titles}
	return render(request, 'activities/assignment_title_keyword_search.html', dictionary)

def assignment_by_type(request):
	return_dict = {'name': 'assignments', 'children': []}
	top_children = []
	for entry in AssignmentType.objects.all():
		top_children.append({'name': entry.name, 'id': entry.id, 'children':[]})
	for tc in top_children:
		lookup_id = tc['id']
		subchildren_objects = AssignmentTitle.objects.filter(assignment_type=lookup_id)
		for entry2 in subchildren_objects:
			subchildren_dict = {}
			subchildren_dict['name'] = entry2.name
			subchildren_dict['id'] = entry2.id
			subchildren_dict['size'] = Assignment.objects.filter(assignment_title=entry2.id).count()
			tc['children'].append(subchildren_dict)

	return_dict['children'] = top_children
	import json
	jstring = json.dumps(return_dict, sort_keys=False, indent=2)
	return HttpResponse(jstring, content_type=u'text/javascript; charset=utf8')

def assignment_sunburst(request):
	return render(request, 'activities/assignment_sunburst.html')

def assignment_bubble(request):
	return render(request, 'activities/assignment_bubble.html')