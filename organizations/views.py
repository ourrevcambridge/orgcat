from django.views.generic import DetailView
from .models import Organization

class OrganizationView(DetailView):
  model         = Organization
  template_name = "organizations/organization-detail.html"

detail = OrganizationView.as_view() 