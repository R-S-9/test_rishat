from django.shortcuts import render
from django.views.generic import View

from .utils import ItemUtil


class ItemStripe(View):
    @staticmethod
    def get(request, item_id):
        return render(
            request=request,
            template_name='payment.html',
            context={
                'data': ItemUtil.product_data(item_id),
                'item_id': str(item_id),
            },
            status=200
        )
