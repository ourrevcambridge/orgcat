from django.conf import settings
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

class Organization(models.Model):
  GEOGRAPHIC_SCOPE_CHOICES = [
    ("intl", "International"),
    ("natl", "National"     ),
    ("regl", "Regional"     ),
    ("stat", "State"        ),
    ("subs", "State Region" ),
    ("city", "City"         )
  ]
  
  name             = models.CharField(max_length=128)
  abbreviation     = models.CharField(max_length=16, blank=True)
  website          = models.URLField()
  facebook         = models.CharField(max_length=128)
  email            = models.EmailField()
  phone_number     = PhoneNumberField(blank=True)
  is_coalition     = models.BooleanField(default=False)
  geographic_scope = models.CharField(max_length=4, choices=GEOGRAPHIC_SCOPE_CHOICES)
  country          = models.CharField(max_length=64)
  region           = models.CharField(max_length=64)
  state            = models.CharField(max_length=64)
  state_region     = models.CharField(max_length=64)
  city             = models.CharField(max_length=64)
  issues           = models.ManyToManyField("Issue")
  description      = models.TextField()
  notes            = models.TextField()
  submitted_by     = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, blank=True, null=True)
  created_at       = models.DateTimeField(auto_now_add=True)
  updated_at       = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Issue(models.Model):
  name = models.CharField(max_length=64)
  
  def __str__(self):
    return self.name

class Contact(models.Model):
  PHONE_TYPE_CHOICES = [
    ("o", "Office"),
    ("m", "Mobile"),
    ("h", "Home")
  ]

  role         = models.CharField(max_length=32, blank=True)
  first_name   = models.CharField(max_length=32)
  last_name    = models.CharField(max_length=32)
  email        = models.EmailField()
  phone_number = PhoneNumberField(blank=True)
  phone_type   = models.CharField(max_length=1, choices=PHONE_TYPE_CHOICES, blank=True)
  location     = models.CharField(max_length=128)
  organization = models.ForeignKey(Organization, models.SET_NULL, null=True, blank=True)

  @property
  def full_name(self):
      return "{0} {1}".format(self.first_name, self.last_name)

  def __str__(self):
    return self.full_name

  