#This is the models.py file for the CITATIONS app
#It handles the citation system for the database, including bibliographic and footnote like entries.
#It also makes use of the built-in django authentication module to record who entered what into the system.

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Bibliography(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    entry = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'bibliographies'
        verbose_name_plural = 'Bibliographies'
    def __unicode__(self):
        return self.entry

class Citation(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=765, blank=True)
    bibliography = models.ForeignKey(Bibliography, null=True, blank=True)
    pages = models.CharField(max_length=765, blank=True)
    canonic_url = models.CharField(max_length=765, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'citations'
    def __unicode__(self):
        return self.title


class Validation(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    auth_user = models.ForeignKey(User, null=True, blank=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    supports = models.NullBooleanField(null=True, blank=True)
    citation = models.ForeignKey(Citation, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'validations'
    def __unicode__(self):
        return u"%s %d" % (self.content_type, self.object_id)