import operator
from django.db import models
from functools import reduce
from unittest.mock import Mock

from app.enums import ProvinceEnum
from .resource_model import ResourceModel, ResourceManager, ResourceQuerySet


class DonorQuerySet(ResourceQuerySet):
    def are_businesses(self):
        '''Return donors that are businesses.
        Individuals are donors with not matching contact_name to donor_name
        '''
        donors = self.exclude(contact_name='').values(
            'id', 'donor_name', 'contact_name')
        org_ids = [d['id']
                   for d in donors if d['donor_name'] != d['contact_name']]
        return self.filter(id__in=org_ids)

    def are_individuals(self):
        '''Return donors that are individuals.
        Individuals are donors with empty contact_name or matching contact_name
        '''
        donors = self.exclude(contact_name='').values(
            'id', 'donor_name', 'contact_name')
        org_ids = [d['id']
                for d in donors if d['donor_name'] != d['contact_name']]
        return self.exclude(id__in=org_ids)


class DonorManager(ResourceManager):
    def get_queryset(self):
        if self.alive_only:
            return DonorQuerySet(self.model).alive()
        return DonorQuerySet(self.model)


class Donor(ResourceModel):
    objects = DonorManager()
    all_objects = DonorManager(alive_only=False)

    donor_name = models.CharField('Donor Name', max_length=255)
    contact_name = models.CharField('Contact Name', blank=True, max_length=255)
    email = models.EmailField('Email')
    want_receipt = models.BooleanField('Want Tax Receipt?', default=True)
    telephone_number = models.CharField(
        'Telephone #', blank=True, max_length=255)
    mobile_number = models.CharField('Mobile #', blank=True, max_length=255)
    address_line_one = models.CharField(
        'Address Line 1', blank=True, max_length=255)
    address_line_two = models.CharField(
        'Address Line 2', blank=True, max_length=255)
    city = models.CharField('City', max_length=255)
    province = models.CharField(
        'Province', choices=ProvinceEnum.choices(), max_length=255)
    postal_code = models.CharField('Postal Code', max_length=10)
    customer_ref = models.CharField(
        'Customer Ref.', blank=True, max_length=255)

    def verified_prop(self):
        verifieds = list(map((lambda x: x.verified), self.donation_set.all()))
        return reduce(operator.and_, verifieds, True)
    verified_prop.short_description = 'Verified?'
    verified = property(verified_prop)

    def is_org(self):
        return self.contact_name != '' and self.contact_name != self.donor_name

    def save(self, *args, **kwargs):
        # donations = self.donation_set.all().prefetch_related('item_set')
        # donation_verified, item_verified = True, True
        # items = []
        # self.verified = True
        # for donation in donations:
        #     if not donation.verified:
        #         self.verified = False
        #         break
        super(Donor, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.donor_name)
