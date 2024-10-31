from src.models.user import User


class Store:

    def __init__(self):
        self.bd = [
            User('Thiago', 'Tester'),
            User('Joao', 'Ruim'),
            User('PO', 'ht'),
            User('JPL', 'fw'),
            User('RG', 'fw'),
            User('JTG', 'fw')
        ]

