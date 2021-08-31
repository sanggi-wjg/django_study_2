class DataSampleVO(object):

    def __init__(self, index: str, rack_code: str, product_code: str, register_date: str):
        self._index = index
        self._rack_code = rack_code
        self._product_code = product_code
        self._register_date = register_date

    def validate(self):
        pass

    @property
    def index(self):
        return self._index

    @property
    def rack_code(self):
        return self._rack_code

    @property
    def product_code(self):
        return self._product_code

    @property
    def register_date(self):
        return self._register_date