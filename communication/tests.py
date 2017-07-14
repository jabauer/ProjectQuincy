"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Letter, Enclosure

class TestLetter(TestCase):
	fixtures = ['organizations.json','individuals.json','coordinate_system.json','continents.json','states.json','locations.json','letters.json']

	def test_str(self):
		l = Letter.objects.first()
		assert unicode(l) == l.title


class TestEnclosure(TestCase):
	fixtures = ['organizations.json','individuals.json','coordinate_system.json','continents.json','states.json','locations.json','letters.json', 'enclosures.json']

	def test_str(self):
		e = Enclosure.objects.first()
		assert unicode(e) == u'%s enclosed in %s' % (e.enclosed_letter, e.main_letter)


class TestCommunicationViews(TestCase):
	fixtures = ['organizations.json','individuals.json','coordinate_system.json','continents.json','states.json','locations.json','letters.json']

	def test_letter_list(self):
		letter_list_url = reverse('letter_list')
		response = self.client.get(letter_list_url)
		assert response.status_code == 200
		for letter in Letter.objects.all():
			self.assertContains(response, letter.title, 
				msg_prefix='letter list should include %s' % letter.title)
		#print response.content
		self.assertContains(response, '%d total' % Letter.objects.count())