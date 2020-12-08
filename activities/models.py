#This is the models.py file for the ACTIVITIES app
#These classes constitute the Organizations and Assignments modules in the database
#Will eventually be expanded to include events.
#Essentially -- anything where a person came to a location for a reason.

from django.db import models
from people.models import Individual
from places.models import Location

class AssignmentType(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'assignment_types'
    def __unicode__(self):
        return self.name


class AssignmentTitle(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    assignment_type = models.ForeignKey(AssignmentType, on_delete=models.PROTECT, null=True)
    temporary = models.NullBooleanField(null=True, blank=True)
    commissioned = models.NullBooleanField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'assignment_titles'
    def __unicode__(self):
        return self.name


class Assignment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    individual = models.ForeignKey(Individual, on_delete=models.PROTECT, null=True, blank=True)
    assignment_title = models.ForeignKey(AssignmentTitle, on_delete=models.PROTECT, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=True, blank=True)
    start_year = models.IntegerField(null=True, blank=True)
    start_certain = models.NullBooleanField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    end_certain = models.NullBooleanField(null=True, blank=True)
    notes = models.TextField(blank=True)
    class Meta:
        db_table = u'assignments'
    def __unicode__(self):
        return u"%s | %s | %s | %d | %d" % (self.individual, self.assignment_title, self.location, self.start_year, self.end_year)


class OrganizationType(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'organization_types'
    def __unicode__(self):
        return self.name


class Organization(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    magazine_sending = models.NullBooleanField(null=True, blank=True)
    organization_type = models.ForeignKey(OrganizationType, on_delete=models.PROTECT, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=True, blank=True)
    org_bio = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'organizations'
    def __unicode__(self):
        return self.name


class OrgEvolutionType(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'org_evolution_types'
    def __unicode__(self):
        return self.name

class OrgEvolution(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    org_1 = models.ForeignKey(Organization, on_delete=models.PROTECT, null=True, related_name='org_1')
    org_2 = models.ForeignKey(Organization, on_delete=models.PROTECT, null=True, related_name='org_2')
    org_evolution_type = models.ForeignKey(OrgEvolutionType, on_delete=models.PROTECT, null=True)
    date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    day_known = models.NullBooleanField(null=True, blank=True)
    month_known = models.NullBooleanField(null=True, blank=True)
    year_known = models.NullBooleanField(null=True, blank=True)
    class Meta:
        db_table = u'org_evolutions'
    def __unicode__(self):
        return u"%s to %s | %s" % (self.org_1, self.org_2, self.org_evolution_type)


class RoleType(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'role_types'
    def __unicode__(self):
        return self.name


class RoleTitle(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=765)
    role_type = models.ForeignKey(RoleType, on_delete=models.PROTECT, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'role_titles'
    def __unicode__(self):
        return self.name


class Member(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    individual = models.ForeignKey(Individual, on_delete=models.PROTECT, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, null=True, blank=True)
    role_title = models.ForeignKey(RoleTitle, on_delete=models.PROTECT, null=True, blank=True)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = u'members'
    def __unicode__(self):
        return u"%s | %s | %s" % (self.individual, self.organization, self.role_title)





