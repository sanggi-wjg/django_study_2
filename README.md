# Django DEMO

### 개발 환경
```
Python 3.8
Django 3.2.6
```

### 추가 패키지
```
pip install django==3.2.6
```

유저 
```
https://docs.djangoproject.com/ko/3.2/topics/auth/
https://han-py.tistory.com/145
https://wikidocs.net/71303
```

### Create App 
```shell script
python manage.py startapp apps
```

### Django Migrate Table
```shell script
python manage.py migrate
```

### Model migrate
```shell script
python manage.py makemigrations apps
python manage.py sqlmigrate apps 0001
python manage.py migrate
```