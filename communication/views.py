# communication/views.py
#places/views.py
#This files contains the view functions for the COMMUNICATION.
#For right now that just means letters . . . 


from django.shortcuts import render, redirect, get_object_or_404
from .models import Letter

import operator

def letter_list(request):
	return render(request, 'communication/letter_list.html', {'letters': Letter.objects.all().order_by('date_sent')})