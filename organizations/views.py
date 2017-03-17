from django.views.generic import DetailView, ListView
from .models import Organization

class OrganizationDetailView(DetailView):
  model         = Organization
  template_name = "organizations/organization-detail.html"

detail = OrganizationDetailView.as_view()

class OrganizationListView(ListView):
  model         = Organization
  template_name = "organizations/organization-list.html"
  context_object_name = "organizations"

list = OrganizationListView.as_view()