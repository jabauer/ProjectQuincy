"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import AssignmentType


class TestAssignmentType(TestCase):
	fixtures = ['assignment_type.json']

	def test_str(self):
		atype = AssignmentType.objects.first()
		assert unicode(atype) == atype.name


class TestActivitiesViews(TestCase):
	fixtures = ['assignment_type.json']

	def test_assignment_type_list(self):
		atype_list_url = reverse('assignment_type_list')
		response = self.client.get(atype_list_url)
		assert response.status_code == 200
		for atype in AssignmentType.objects.all():
			self.assertContains(response, atype.name, 
				msg_prefix='assignment type list should include %s' % atype.name)
			self.assertContains(response, reverse('assignment_type_detail', args=[atype.id]), 
				msg_prefix='assignment type list should include %s' % atype.id)
		#print response.content
		self.assertContains(response, '%d total' % AssignmentType.objects.count())

	def test_assignment_type_detail(self):
		atypeBAD_detail_url = reverse('assignment_type_detail', args=[1])
		response = self.client.get(atypeBAD_detail_url)
		assert response.status_code == 404
		diplomat = AssignmentType.objects.get(pk=676005164)
		atypeGOOD_detail_url = reverse('assignment_type_detail', args=[diplomat.pk])
		response = self.client.get(atypeGOOD_detail_url)
		assert response.status_code == 200