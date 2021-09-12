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
```
# Django Unit Test
python manage.py test sample.tests --keepdb

# Django DiscoverRunner  
https://adamj.eu/tech/2020/09/05/what-happens-when-you-run-manage.py-test/

# pytest
pytest sample/test/test_models.py 
(https://pytest-django.readthedocs.io/en/latest)
```

## 참고
#### 유저 
```
https://docs.djangoproject.com/ko/3.2/topics/auth/
https://han-py.tistory.com/145
https://wikidocs.net/71303
```