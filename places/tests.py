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
		stype = State.objects.create(name="New Jersey")
		in_state = InState.objects.create(location=ltype, state=stype)
		assert unicode(in_state) == u'%s in %s' % (in_state.location, in_state.state)

class TestEmpire(TestCase):

	def test_str(self):
		etype = Empire.objects.create(name="Galactic Empire")
		assert unicode(etype) == etype.name

class TestInEmpire(TestCase):

	def test_str(self):
		stype = State.objects.create(name="Corusant")
		etype = State.objects.create(name="Galactic Empire")
		in_empire = InEmpire.objects.create(state=stype, empire=etype)
		assert unicode(in_empire) == u'%s in %s' % (in_empire.state, in_empire.empire)
		