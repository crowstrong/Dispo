from django.views.generic import TemplateView
from django.http import HttpResponse
from core.tasks import task_request, get_price, order_request


class DispoHomePage(TemplateView):
    template_name = "index.html"


class Error404(TemplateView):
    template_name = "errors/not-found.html"


def start_task(request):
    task_request.delay()
    return HttpResponse("Task is started")


def price_task(request):
    get_price.delay()
    return HttpResponse("Price task is started, waiting for quotation.")


def order_registration(request):
    order_request.delay()
    return HttpResponse("Task is started")
