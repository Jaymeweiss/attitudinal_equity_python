DEFAULT_RANKING = 0
DEFAULT_AE = 0

class Brand:
    def __init__(self, brand, value, table_index, ranking=DEFAULT_RANKING, attitudinal_equity=DEFAULT_AE):
        self.brand = brand
        self.value = value
        self.ranking = ranking
        self.attitudinal_equity = attitudinal_equity
        self.table_index = table_index
