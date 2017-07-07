"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from .models import AssignmentType

class TestAssignmentType(TestCase):
	fixtures = ['assignment_type.json']

	def test_str(self):
		atype = AssignmentType.objects.first()
		assert unicode(atype) == atype.name
