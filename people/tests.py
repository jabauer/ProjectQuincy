"""
This file contains the tests for the PEOPLE APP
"""

from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Individual, ResidenceType, Residence, OccupationType, OccupationTitle, Occupation, RelationshipType, Relationship
from places.models import State, Location
from citations.models import Validation
from django.contrib.contenttypes.models import ContentType

class TestIndividual(TestCase):
	fixtures = ['adams_family.json', 'adams_states.json', 'continents.json']

	def test_str(self):
		i = Individual.objects.first()
		assert unicode(i) == i.name

class TestResidenceType(TestCase):

	def test_str(self):
		rt = ResidenceType.objects.create(name='Birth Place')
		assert unicode(rt) == rt.name

class TestResidence(TestCase):
	fixtures = ['adams_family.json', 'adams_states.json','adams_locations.json',
	'continents.json','coordinate_system.json']

	def test_str(self):
		i = Individual.objects.get(pk=1)
		l = Location.objects.get(pk=334)
		r = Residence.objects.create(individual=i, location=l, birth_place=True)
		assert unicode(r) == u'%s at %s' % (r.individual, r.location)

class TestOccuptationType(TestCase):

	def test_str(self):
		oty = OccupationType.objects.create(name="legal")
		assert unicode(oty) == oty.name

class TestOccupationTitle(TestCase):

	def test_str(self):
		oti = OccupationTitle.objects.create(name='lawyer')
		assert unicode(oti) == oti.name

class TestOccupation(TestCase):
	# fixtures = ['adams_family.json', adams]

	def test_str(self):
		o = Occupation.objects.create(individual=Individual.objects.create(name="Abigail Adams"), 
			occupation_title=OccupationTitle.objects.create(name="diplomat"))
		assert unicode(o) == u'%s, %s' % (o.individual, o.occupation_title)

class TestRelationshipType(TestCase):

	def test_str(self):
		rt = RelationshipType.objects.create(name="Dearest Friend")
		assert unicode(rt) == rt.name

class TestRelationship(TestCase):

	def test_str(self):
		r = Relationship.objects.create(individual_id_1=Individual.objects.create(name="Abigail"),
			individual_id_2=Individual.objects.create(name="John"), 
			relationship_type=RelationshipType.objects.create(name="Dearest Friend"))
		assert unicode(r) == u'%s and %s' % (r.individual_id_1, r.individual_id_2)

class TestPeopleViews(TestCase):
	fixtures = ['adams_family.json', 'adams_states.json', 'continents.json']

	def test_individual_list(self):
		individual_list_url = reverse('individual_list')
		response = self.client.get(individual_list_url)
		assert response.status_code == 200
		for i in Individual.objects.all():
			self.assertContains(response, i.name,
				msg_prefix='individual list should include %s' % i.name)
		self.assertContains(response, '%d total' %Individual.objects.count())

	def test_individual_detail(self):
		jqa = Individual.objects.get(pk=14)
		footnotes = Validation.objects.all()
		i_detail_url = reverse('individual_detail', args=[jqa.pk])
		response = self.client.get(i_detail_url)
		assert response.status_code == 200
		print response.content

"""
TESTS STILL TO WRITE

On Views:
- add to test_individual_list
	- order_by results
- add to test_individual_detail
	- Validations
- test_individual_search

"""










