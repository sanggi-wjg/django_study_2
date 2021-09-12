import pytest
from django.test import TestCase


class StocksTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        from sample.models import Stocks
        cls.stocks = Stocks.objects.filter(stock_code__in = ['033780', '035420', '005930'])

    def test_len(self):
        assert 4 == len(self.stocks)
