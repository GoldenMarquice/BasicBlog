from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutMeView(TemplateView):
    template_name = "pages/aboutme.html"