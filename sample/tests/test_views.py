from django.test import TestCase, SimpleTestCase
from django.urls import reverse


class SampleViewTest(TestCase):

    def test_status(self):
        url = reverse('SampleMulti')
        response = self.client.get(url)

        print(f'URL: {url} / status_code: {response.status_code}')
        assert 200 == response.status_code \
               or 302 == response.status_code
