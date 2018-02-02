#This is the models.py file for the PEOPLE app
#The classes modeled here describe the interactions of individuals.
#It relies on information from the PLACES app


from django.db import models
from places.models import Location, State

# Create your models here.

class Individual(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    sex = models.CharField(max_length=765, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    state = models.ForeignKey(State, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    sort_name = models.CharField(max_length=765, blank=True)
    american = models.NullBooleanField(null=True, blank=True)
    birth_day_known = models.NullBooleanField(null=True, blank=True)
    birth_month_known = models.NullBooleanField(null=True, blank=True)
    birth_year_known = models.NullBooleanField(null=True, blank=True)
    death_day_known = models.NullBooleanField(null=True, blank=True)
    death_month_known = models.NullBooleanField(null=True, blank=True)
    death_year_known = models.NullBooleanField(null=True, blank=True)
    class Meta:
        db_table = u'individuals'
    def __unicode__(self):
    	return self.name


class ResidenceType(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    temporary = models.NullBooleanField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'residence_types'
    def __unicode__(self):
    	return self.name

class Residence(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    individual = models.ForeignKey(Individual, null=True)
    location = models.ForeignKey(Location, null=True)
    residence_type = models.ForeignKey(ResidenceType, null=True, blank=True)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    birth_place = models.NullBooleanField(null=True, blank=True)
    death_place = models.NullBooleanField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'residences'
    def __unicode__(self):
    	return u'%s at %s' % (self.individual, self.location)


class OccupationType(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'occupation_types'
    def __unicode__(self):
    	return self.name


class OccupationTitle(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    occupation_type = models.ForeignKey(OccupationType, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'occupation_titles'
    def __unicode__(self):
    	return self.name


class Occupation(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    individual = models.ForeignKey(Individual, null=True)
    occupation_title = models.ForeignKey(OccupationTitle, null=True)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'occupations'
    def __unicode__(self):
    	return u'%s, %s' % (self.individual, self.occupation_title)

class RelationshipType(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'relationship_types'
    def __unicode__(self):
    	return self.name

class Relationship(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    individual_id_1 = models.ForeignKey(Individual, null=True, db_column='individual_id_1', related_name='individual_1')
    individual_id_2 = models.ForeignKey(Individual, null=True, db_column='individual_id_2', related_name='individual_2')
    relationship_type = models.ForeignKey(RelationshipType, null=True)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'relationships'
    def __unicode__(self):
    	return u'%s and %s' % (self.individual_id_1, self.individual_id_2)
