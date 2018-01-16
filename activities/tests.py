"""
This is the tests.py file for the ACTIVITIES app
These tests handle models and views related to the Organizations
	and Assigments Modules
"""

from django.core.urlresolvers import reverse
from django.test import TestCase


from .models import AssignmentType, AssignmentTitle, Assignment, OrganizationType, Organization, OrgEvolutionType, OrgEvolution, RoleType, RoleTitle, Member
from people.models import Individual
from places.models import Location


class TestAssignmentType(TestCase):
	fixtures = ['assignment_type.json']

	def test_str(self):
		atype = AssignmentType.objects.first()
		assert unicode(atype) == atype.name

class TestAssignmentTitle(TestCase):

	def test_str(self):
		atitle = AssignmentTitle.objects.create(name="Envoy Extraordinaire")
		assert unicode(atitle) == atitle.name

class TestAssignment(TestCase):

	def test_str(self):
		i = Individual.objects.create(name="Abigail Adams")
		atitle = AssignmentTitle.objects.create(name="One who knows all")
		loc = Location.objects.create(name="All of time and space")
		assignment = Assignment.objects.create(individual=i, assignment_title=atitle, location=loc, 
			start_year=1744, end_year=1818)
		assert unicode(assignment) == u'%s | %s | %s | %d | %d' % (assignment.individual, assignment.assignment_title, assignment.location, assignment.start_year, assignment.end_year)

class TestOrganizationType(TestCase):

	def test_str(self):
		otype = OrganizationType.objects.create(name="Fan Club")
		assert unicode(otype) == otype.name

class TestOrganization(TestCase):

	def test_str(self):
		org = Organization.objects.create(name="Squirrel Girl Appreciation Society")
		assert unicode(org) == org.name

class TestOrgEvolutionType(TestCase):

	def test_str(self):
		orgevtype = OrgEvolutionType.objects.create(name="Mutual Appreciation")
		assert unicode(orgevtype) == orgevtype.name

class TestOrgEvolution(TestCase):
	"""docstring for TestOrgEvolution"""
	def test_str(self):
		sg = Organization.objects.create(name="Squirrel Girl Appreciation Society")
		ch = Organization.objects.create(name="Chipmunk Hunk Appreciation Society")
		ma = OrgEvolutionType.objects.create(name="Mutual Appreciation")
		koi = OrgEvolution.objects.create(org_1=sg, org_2=ch, org_evolution_type=ma)
		assert unicode(koi) == u'%s to %s | %s' % (koi.org_1, koi.org_2, koi.org_evolution_type)

class TestRoleType(TestCase):

	def test_str(self):
		rtype = RoleType.objects.create(name="legislative")
		assert unicode(rtype) == rtype.name

class TestRoleTitle(TestCase):

	def test_str(self):
		rtitle = RoleTitle.objects.create(name="senator")
		assert unicode(rtitle) == rtitle.name

class TestMember(TestCase):

	def test_str(self):
		person = Individual.objects.create(name="Leia Organa")
		org = Organization.objects.create(name="The Rebellion")
		title = RoleTitle.objects.create(name="General")
		princess = Member.objects.create(individual=person, organization=org, role_title=title)
		assert unicode(princess) == u'%s | %s | %s' % (princess.individual, princess.organization, princess.role_title)
		

class TestActivitiesViews(TestCase):
	fixtures = ['assignment_type.json', 'assignment_titles.json']

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

	def test_assignment_title_list(self):
		"""
		This test does not work for titles with "'" in them, but that is because of 
		how django is escaping the character from the fixture. Will come back and fix sometime
		so it works for everything.
		"""
		atitle_list_url = reverse('assignment_title_list')
		response = self.client.get(atitle_list_url)
		assert response.status_code == 200
		#print response.content
		for atitle in AssignmentTitle.objects.all():
			self.assertContains(response, atitle.name,
				msg_prefix='assignment title list should include %s' % atitle.name)
			self.assertContains(response, reverse('assignment_title_detail', args=[atitle.id]),
				msg_prefix='assignment title list should include %s' % atitle.id)
		self.assertContains(response, '%d total' % AssignmentTitle.objects.count())

	def test_assignment_title_detail(self):
		atitleBAD_detail_url = reverse('assignment_title_detail', args=[567890])
		response = self.client.get(atitleBAD_detail_url)
		assert response.status_code == 404
		consul = AssignmentTitle.objects.get(pk=18)
		atitleGOOD_detail_url = reverse('assignment_title_detail', args=[consul.pk])
		response = self.client.get(atypeGOOD_detail_url)
		#print response.content
		assert response.status_code == 200

	def test_assignment_sunburst(self):
		sunburst = reverse('assignment_sunburst')
		response = self.client.get(sunburst)
		assert response.status_code == 200
		#print response.content

	def test_assignment_circle_pack(self):
		circle = reverse('assignment_bubble')
		response = self.client.get(circle)
		assert response.status_code == 200






		