from typing import List

from django.db import models


class StockPriceQuerySet(models.QuerySet):

    def get_stocks_price(self, stocks: List[models.Model]) -> models.Model:
        # stock_prices = self.values('close_price', 'date', 'stock_').filter(stocks_id__in = stocks).order_by('date')
        # return stock_prices
        pass
