from django.urls import path

from core.views import price_task, send_invoices_all, start_task, room, support

app_name = "core"

urlpatterns = [
    path("support/", support, name="support"),
    path('<str:room_name>/', room, name='room'),
    path("start_task/", start_task, name="start_task"),
    path("price_task/", price_task, name="price_task"),
    path("send_invoices_all/", send_invoices_all, name="send_invoices_all"),
]
