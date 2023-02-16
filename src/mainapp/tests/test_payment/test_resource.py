from django.test import TestCase, RequestFactory

from ...models import Item
from ...mainpage.resource import MainPage


class MainPageTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()

    def test_get(self):
        request = self.factory.get('')
        request.content_type = 'application/json'
        response = MainPage.as_view()(request)

        assert response.status_code == 200
