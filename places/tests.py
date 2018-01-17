"""
This is the tests.py file for the PLACES app
These tests handle modles and views related to the
	Locations Module
"""

from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import CoordinateSystem, Location, Region, InRegion, Continent, State, InState, Empire, InEmpire

class TestCoordinateSystem(TestCase):

	def test_str(self):
		cstype = CoordinateSystem.objects.create(short_name="WSG84")
		assert unicode(cstype) == cstype.short_name

class TestLocation(TestCase):

	def test_str(self):
		ltype = Location.objects.create(name="Braintree")
		cstype = CoordinateSystem.objects.create(short_name="WSG84")
		assert unicode(ltype) == ltype.name

class TestRegion(TestCase):

	def test_str(self):
		rtype = Region.objects.create(name="Inner Rim")
		assert unicode(rtype) == rtype.name

class TestInRegion(TestCase):

	def test_str(self):
		ltype = Location.objects.create(name="Jakku")
		rtype = Region.objects.create(name="Inner Rim")
		in_region = InRegion.objects.create(region=rtype, location=ltype)
		assert unicode(in_region) == u'%s in %s' % (in_region.location, in_region.region)

class TestContinent(TestCase):

	def test_str(self):
		ctype = Continent.objects.create(name="North America")
		assert unicode(ctype) == ctype.name


class TestState(TestCase):

	def test_str(self):
		ctype = Continent.objects.create(name="North America")
		stype = State.objects.create(name="Haiti", continent=ctype)
		assert unicode(stype) == stype.name

class TestInState(TestCase):

	def test_str(self):
		ltype = Location.objects.create(name="Asbury Park")
		ctype = Continent.objects.create(name="North America")
		stype = State.objects.create(name="New Jersey", continent=ctype)
		in_state = InState.objects.create(location=ltype, state=stype)
		assert unicode(in_state) == u'%s in %s' % (in_state.location, in_state.state)

class TestEmpire(TestCase):

	def test_str(self):
		etype = Empire.objects.create(name="Galactic Empire")
		assert unicode(etype) == etype.name

class TestInEmpire(TestCase):

	def test_str(self):
		ctype = Continent.objects.create(name="Corusant")
		stype = State.objects.create(name="Corusant", continent=ctype)
		etype = Empire.objects.create(name="Galactic Empire")
		in_empire = InEmpire.objects.create(state=stype, empire=etype)
		assert unicode(in_empire) == u'%s in %s' % (in_empire.state, in_empire.empire)

class TestPlacesViews(TestCase):
	fixtures = ['coordinatesystem.json', 'continents.json', 'states.json', 'locations.json', 'regions.json']

#The detail tests will need to be redone once class based views are instituted


	def test_continent_list(self):
		clist_url = reverse('continent_list')
		response = self.client.get(clist_url)
		assert response.status_code == 200
		for c in Continent.objects.all():
			self.assertContains(response, c.name, 
				msg_prefix='continent list should include %s' % c.name)
			self.assertContains(response, reverse('continent_detail', args=[c.id]),
				msg_prefix='continent list should include %s ' % c.id)
			self.assertContains(response, '%d total' % Continent.objects.count())
			# print response.content

	def test_continent_detail(self):
		cBAD_detail_url = reverse('continent_detail', args=[1])
		response = self.client.get(cBAD_detail_url)
		assert response.status_code == 404
		africa = Continent.objects.get(pk=432531999)
		cGOOD_detail_url = reverse('continent_detail', args=[africa.pk])
		response = self.client.get(cGOOD_detail_url)
		assert response.status_code == 200

	def test_state_list(self):
		slist_url = reverse('state_list')
		response = self.client.get(slist_url)
		assert response.status_code == 200
		for s in State.objects.all():
			self.assertContains(response, s.name,
				msg_prefix='state list should include %s' % s.name)
			self.assertContains(response, reverse('state_detail', args=[s.id]),
				msg_prefix='state list should include %s' % s.id)
			self.assertContains(response, '%d total' % State.objects.count())
			# print response.content

	def test_state_detail(self):
		sBAD_detail_url = reverse('state_detail', args=[1])
		response = self.client.get(sBAD_detail_url)
		assert response.status_code == 404
		columbia = State.objects.get(pk=62)
		sGOOD_detail_url = reverse('state_detail', args=[columbia.pk])
		response = self.client.get(sGOOD_detail_url)
		assert response.status_code == 200

	def test_location_list(self):
		loclist_url = reverse('location_list')
		response = self.client.get(loclist_url)
		assert response.status_code == 200
		for l in Location.objects.all():
			self.assertContains(response, l.name,
				msg_prefix='location list should include %s' % l.name)
			self.assertContains(response, reverse('location_detail', args=[l.id]),
				msg_prefix='location list should include %s' % l.id)
			self.assertContains(response, '%d total' % Location.objects.count())
			# print response.content

	def test_location_detail(self):
		locBAD_detail_url = reverse('location_detail', args=[1])
		response = self.client.get(locBAD_detail_url)
		assert response.status_code == 404
		quincy = Location.objects.get(pk=334)
		locGOOD_detail_url = reverse('location_detail', args=[quincy.pk])
		response = self.client.get(locGOOD_detail_url)
		assert response.status_code == 200

	def test_region_list(self):
		rlist_url = reverse('region_list')
		response = self.client.get(rlist_url)
		assert response.status_code == 200
		for r in Region.objects.all():
			self.assertContains(response, r.name,
				msg_prefix='region list should include %s' % r.name)
			self.assertContains(response, reverse('region_detail', args=[r.id]),
				msg_prefix='region list should include %s' % r.id)
			self.assertContains(response, '%d total' % Region.objects.count())
			# print response.content

	def test_region_detail(self):
		rBAD_detail_url = reverse('region_detail', args=[5678])
		response = self.client.get(rBAD_detail_url)
		assert response.status_code == 404
		carribean = Region.objects.get(pk=1)
		rGOOD_detail_url = reverse('region_detail', args=[carribean.pk])
		response = self.client.get(rGOOD_detail_url)
		assert response.status_code == 200

	def test_location_circlepack(self):
		circle = reverse('location_circlepack')
		response = self.client.get(circle)
		assert response.status_code == 200

	def test_location_dendrogram(self):
		den = reverse('location_dendrogram')
		response = self.client.get(den)
		assert response.status_code == 200



















