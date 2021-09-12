import pytest
import pandas as pd

from sample.models import Stocks, StockPrice


@pytest.mark.django_db
class TestStocks:

    def test_stocks(self):
        stocks = Stocks.objects.filter(stock_code__in = ['005930', '035420', '033780']).order_by('id')

        for stock, name in zip(stocks, ['KT&G', 'NAVER', '삼성전자']):
            assert stock.stock_name == name


@pytest.mark.django_db
class TestStockPrice:

    def test_stock_price(self):
        stocks = Stocks.objects.filter(stock_code__in = ['005930'])
        stock_prices = StockPrice.objects.values('close_price', 'date').filter(stocks_id__in = stocks).order_by('date')

        df = pd.DataFrame()
        df['SamSung'] = [s['close_price'] for s in stock_prices]
        df['Date'] = [s['date'] for s in stock_prices]
        print(df.tail(n = 20))
