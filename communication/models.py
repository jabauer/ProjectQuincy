#This is the models.py file for the COMMUNICATION app
#It contains models for letters and enclosures
#It will be expanded to include other types of documents

from django.db import models
from places.models import Location
from people.models import  Individual
from activities.models import Organization

class Letter(models.Model):
    id = models.AutoField(primary_key=True)
    from_individual = models.ForeignKey(Individual, null=True, blank=True, related_name='individual_from')
    from_organization = models.ForeignKey(Organization, null=True, blank=True, related_name='organization_from')
    from_location = models.ForeignKey(Location, null=True, blank=True, related_name='location_from')
    to_individual = models.ForeignKey(Individual, null=True, blank=True, related_name='individual_to')
    to_organization = models.ForeignKey(Organization, null=True, blank=True, related_name='organization_to')
    to_location = models.ForeignKey(Location, null=True, blank=True, related_name='location_to')
    circular = models.NullBooleanField(null=True, blank=True)
    date_sent = models.DateField(null=True, blank=True)
    date_received = models.DateField(null=True, blank=True)
    date_docketed = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    title = models.CharField(max_length=765, blank=True)
    sent_day_known = models.NullBooleanField(null=True, blank=True)
    sent_month_known = models.NullBooleanField(null=True, blank=True)
    sent_year_known = models.NullBooleanField(null=True, blank=True)
    received_day_known = models.NullBooleanField(null=True, blank=True)
    received_month_known = models.NullBooleanField(null=True, blank=True)
    received_year_known = models.NullBooleanField(null=True, blank=True)
    docketed_day_known = models.NullBooleanField(null=True, blank=True)
    docketed_month_known = models.NullBooleanField(null=True, blank=True)
    docketed_year_known = models.NullBooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'letters'
    def __unicode__(self):
        return self.title


class Enclosure(models.Model):
    id = models.AutoField(primary_key=True)
    main_letter = models.ForeignKey(Letter, null=True, blank=True, related_name='letter_1')
    enclosed_letter = models.ForeignKey(Letter, null=True, related_name='letter_2')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'enclosures'
    def __unicode__(self):
        return u'%s enclosed in %s' % (self.enclosed_letter, self.main_letter)