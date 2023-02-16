from dotenv import load_dotenv
from django.http import JsonResponse
from django.views.generic import View

from .utils import PaymentUtil


load_dotenv()


class Payment(View):
    @staticmethod
    def get(request, buy_id, currency):
        session_response, status = PaymentUtil().create_session_stripe(
            buy_id, currency
        )
        return JsonResponse(
            {'sessionId': session_response},
            status=status,
            safe=False,
        )
