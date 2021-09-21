# Django DEMO

## 환경
#### 개발 환경
```
Python 3.8
Django 3.2.6
```
#### Python 패키지
```
pip install django==3.2.6

pip install openpyxl
(https://openpyxl.readthedocs.io/en/stable/index.html)

pip install XlsxWriter
(https://xlsxwriter.readthedocs.io/)

pip install django-debug-toolbar
(https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

pip install djangorestframework
(https://www.django-rest-framework.org/)

pip install dash
pip install pandas
pip install django_plotly_dash
(https://dash.plotly.com/) 
(https://django-plotly-dash.readthedocs.io/en/latest/)
(https://plotly.com/python/)

pip install markdown django-filter pygments pytest-django colorful_print==0.0.4 
```
#### jQuery 패키지
```
jquery uploader
https://github.com/danielm/uploader
```

## Django Commands
#### Create App 
```shell script
python manage.py startapp apps
```
#### Django Migrate Table
```shell script
python manage.py migrate
```
#### Model migrate
```shell script
python manage.py makemigrations apps
python manage.py sqlmigrate apps 0001
python manage.py migrate
```

## Django Test
```shell script
# Django Unit Test
python manage.py test sample.tests --keepdb

# Django DiscoverRunner  
https://adamj.eu/tech/2020/09/05/what-happens-when-you-run-manage.py-test/

# pytest
pytest sample/test/test_models.py
(https://docs.pytest.org/en/6.2.x/)
(https://pytest-django.readthedocs.io/en/latest)
```

```shell script
# test data
https://github.com/FinanceData/FinanceDataReader
```

## Redis
```shell script
pip install django-redis

docker pull redis:6.2.5
docker run --name demo-redis -p 6379:6379 -d redis:6.2.5 redis-server --appendonly yes
docker exec -it demo-redis bash
redis-cli -p 6379
```
```python
# settings.py
CACHES = {
    "default": {
        "BACKEND" : "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.10.204:6379",
        "OPTIONS" : {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# views.py
from django.core.cache import cache

fromcache = cache.get('stock_price_353')
if fromcache is None:
    stock_price = StockPrice.objects.filter(stocks_id = Stocks.objects.get(id = '353'))
    cache.set('stock_price_353', stock_price, 60 * 60)
else:
    stock_price = fromcache
```

```shell script
root@732d8cd6eb27:/data# redis-cli -p 6379
127.0.0.1:6379> keys *
1) ":1:stock_price_353"
127.0.0.1:6379>

# django-redis package
https://github.com/jazzband/django-redis

# Docker redis 명령어
http://redisgate.kr/redis/education/docker_intro.php
```

## 참고
#### 유저 
```shell script
https://docs.djangoproject.com/ko/3.2/topics/auth/
https://han-py.tistory.com/145
https://wikidocs.net/71303
```