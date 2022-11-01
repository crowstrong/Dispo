from django.forms import ModelForm
from shipper.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

    @staticmethod
    def normalize_text(text: str) -> str:
        return text.strip().capitalize()
