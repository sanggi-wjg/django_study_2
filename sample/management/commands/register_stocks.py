import FinanceDataReader as fdr

from django.core.management import BaseCommand
from pandas import Series

from sample.models import Stocks


# class StocksVO(object):
#
#     def __init__(self, code: str, name: str):
#         self._code = code
#         self._name = name
#
#     @property
#     def code(self):
#         return self._code
#
#     @property
#     def name(self):
#         return self._name


class Command(BaseCommand):
    help = 'Register KOSPI Stock'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = fdr.StockListing('KOSPI')
        dataset = []

        for idx, series in df.iterrows():
            if isinstance(series['Sector'], str) and isinstance(series['Industry'], str):
                dataset.append(
                    Stocks(stock_code = series['Symbol'], stock_name = series['Name'])
                )

        Stocks.objects.bulk_create(dataset)
