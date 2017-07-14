"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Bibliography, Citation, Validation


class TestBibliography(TestCase):
	fixtures = ['bibliography.json']

	def test_str(self):
		bib = Bibliography.objects.first()
		assert unicode(bib) == bib.entry


class TestCitation(TestCase):
	fixtures = ['bibliography.json','citations.json']

	def test_str(self):
		cite = Citation.objects.first()
		assert unicode(cite) == cite.title


class TestValidation(TestCase):
	fixtures = ['bibliography.json','citations.json','users.json','validations.json']

	def test_str(self):
		valid = Validation.objects.first()
		assert unicode(valid) == u"%s %d" % (valid.content_type, valid.object_id)
