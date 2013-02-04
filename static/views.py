#These views just call templates for static pages. 
#Pages like About, Acknowledgements, Home, etc that do no pull data from the system

from django.shortcuts import render

def about(request):
	return render(request, 'static/about.html')

def acknowledgements(request):
	return render(request, 'static/acknowledgements.html')

def explore(request):
	return render(request, 'static/explore.html')

def home(request):
	return render(request, 'static/home.html')