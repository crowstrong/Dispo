from django.forms import ModelForm
from django import forms
from shipper.models import Order


class OrderForm(ModelForm):
    loading_date = forms.DateTimeField(
        label="Loading Date/Time",
        widget=forms.DateTimeInput(
            format="%Y-%m-%dT%H:%M",
            attrs={
                'type': 'datetime-local',
            }),
        input_formats=("%Y-%m-%dT%H:%M",),
    )
    delivery_date = forms.DateTimeField(
        label="Delivery Date/Time",
        widget=forms.DateTimeInput(
            format="%Y-%m-%dT%H:%M",
            attrs={
                'type': 'datetime-local',
            }),
        input_formats=("%Y-%m-%dT%H:%M",),
    )

    class Meta:
        model = Order
        fields = "__all__"
