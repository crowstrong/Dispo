import json

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView

from core.tasks import get_price, send_invoices, task_request


class DispoHomePage(TemplateView):
    template_name = "index.html"


class Error404(TemplateView):
    template_name = "errors/not-found.html"


def support(request):
    return render(request, "tools/room_enter.html")


def room(request, room_name):
    return render(request, "tools/chatroom.html", {"room_name_json": mark_safe(json.dumps(room_name))})


def start_task(request):
    task_request.delay()
    return HttpResponse("Task is started")


def price_task(request):
    get_price.delay()
    return HttpResponse("Price task is started, waiting for quotation.")


def send_invoices_all(request):
    send_invoices.delay()
    return HttpResponse("Sent")
