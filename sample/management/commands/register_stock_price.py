import FinanceDataReader as fdr

from django.core.management import BaseCommand

from sample.models import StockPrice, Stocks


class Command(BaseCommand):
    help = 'Register KOSPI Stock Price'

    def add_arguments(self, parser):
        parser.add_argument('stock_code', type = str, help = 'stock code')

    def handle(self, *args, **options):
        stock_code = options['stock_code']
        stock = Stocks.objects.get(stock_code = stock_code)
        df = fdr.DataReader(stock_code)

        dataset = []

        for date, series in df.iterrows():
            dataset.append(
                StockPrice(stocks_id = stock,
                           open_price = series['Open'],
                           high_price = series['High'],
                           low_price = series['Low'],
                           close_price = series['Close'],
                           date = date.strftime('%Y-%m-%d')
                           )
            )

        StockPrice.objects.bulk_create(dataset)
