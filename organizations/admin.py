from django.contrib import admin
from .models import Organization, Issue, Contact

class IssueInline(admin.StackedInline):
  model = Issue

class ContactInline(admin.StackedInline):
  model = Contact

class OrganizationAdmin(admin.ModelAdmin):
  inlines = (ContactInline,)

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Issue)
admin.site.register(Contact)