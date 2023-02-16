import stripe

from django.conf import settings
from dotenv import load_dotenv

from ..item import ItemDAO

load_dotenv()


class PaymentUtil:
    def __init__(self):
        self.api_key = settings.API_KEY_STRIPE

    def create_session_stripe(self, buy_id: int, currency: str) -> {dict, int}:
        """Создание сессии на покупку в stripe"""
        try:
            buy_item = ItemDAO.get_item_by_id(buy_id)

            if not buy_item:
                return {"data": None}

            stripe.api_key = self.api_key
            session = None

            for item in buy_item:
                if currency == 'usd':
                    price = item.price_usd
                else:
                    price = item.price_rub

                session = stripe.checkout.Session.create(
                    success_url="http://127.0.0.1:8000",
                    cancel_url="http://127.0.0.1:8000",
                    payment_method_types=[
                        'card',
                    ],
                    line_items=[
                        {
                            'price_data': {
                                'currency': currency,
                                'unit_amount': int(price*100),
                                'product_data': {
                                    'name': item.name,
                                },
                            },
                            'quantity': 1,
                        },
                    ],
                    mode="payment",
                )
            return session['id'], 303
        except Exception as _ex:
            return {'error': str(_ex)}, 400
