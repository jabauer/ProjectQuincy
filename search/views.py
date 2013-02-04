# Create your views here.
from django.shortcuts import render

def keyword_search(request):
	return render(request, 'search/keyword_search.html')