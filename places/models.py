#This is the models.py file for the Places App
#The models described here constitute the location module of the database
#This is also the only app that does not require other apps for foreign keys.

from django.db import models


class CoordinateSystem(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    short_name = models.CharField(max_length=150)
    long_name = models.CharField(max_length=765, blank=True)
    notes = models.TextField(blank=True)
    reference = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'coordinate_systems'
    def __unicode__(self):
        return self.short_name


class Location(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    notes = models.TextField(blank=True)
    coordinate_system = models.ForeignKey(CoordinateSystem, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'locations'
    def __unicode__(self):
        return self.name


class Region(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'regions'
    def __unicode__(self):
        return self.name


class InRegion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'in_regions'
    def __unicode__(self):
        return u'%s in %s' % (self.location, self.region)


class Continent(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'continents'
    def __unicode__(self):
        return self.name


class State(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    continent = models.ForeignKey(Continent)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'states'
    def __unicode__(self):
        return self.name


class InState(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=True)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'in_states'
    def __unicode__(self):
        return u'%s in %s' % (self.location, self.state)


class Empire(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'empires'
    def __unicode__(self):
        return self.name


class InEmpire(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=True)
    empire = models.ForeignKey(Empire, on_delete=models.PROTECT, null=True)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'in_empires'
    def __unicode__(self):
        return u'%s in %s' % (self.state, self.empire)