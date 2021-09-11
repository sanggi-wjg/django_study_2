import datetime

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 100, blank = True, default = '')
    code = models.TextField()
    linenos = models.BooleanField(default = False)
    language = models.CharField(choices = LANGUAGE_CHOICES, default = 'python', max_length = 100)
    style = models.CharField(choices = STYLE_CHOICES, default = 'friendly', max_length = 100)

    class Meta:
        ordering = ['created']


class Stocks(models.Model):
    id = models.AutoField(primary_key = True, db_column = 'id')

    stock_code = models.CharField(max_length = 10, unique = True, null = False, db_column = 'stock_code')
    stock_name = models.CharField(max_length = 50, unique = True, null = False, db_column = 'stock_name')

    class Meta:
        managed = True
        db_table = 'stocks'
        ordering = ['id']


class StockPrice(models.Model):
    id = models.AutoField(primary_key = True, db_column = 'id')

    open_price = models.IntegerField(blank = False, null = False, db_column = 'open_price')
    high_price = models.IntegerField(blank = False, null = False, db_column = 'high_price')
    low_price = models.IntegerField(blank = False, null = False, db_column = 'low_price')
    close_price = models.IntegerField(blank = False, null = False, db_column = 'close_price')
    date = models.DateField(blank = False, null = False, db_column = 'date')

    stocks_id = models.ForeignKey(Stocks, on_delete = models.DO_NOTHING, db_column = 'stocks_id')

    class Meta:
        managed = True
        db_table = 'stock_price'
        ordering = ['id']
