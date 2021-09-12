import pytest
from amk_demo import settings
from amk_demo.settings import develop


@pytest.fixture(scope = 'session')
def django_db_setup():
    settings.DATABASES = develop.DATABASES
