from django.views.generic import TemplateView

class AboutView(TemplateView):
  template_name = "core/about.html"

about = AboutView.as_view()