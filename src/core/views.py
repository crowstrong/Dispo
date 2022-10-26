from django.views.generic import TemplateView


class DispoHomePage(TemplateView):
    template_name = "index.html"


class Error404(TemplateView):
    template_name = "errors/not-found.html"
