from typing import List
from inventory_report.product import Product


class Inventory:
    def __init__(self, data: List[Product] | None = None) -> None:
        self._data = data if data is not None else []

    def add_data(self, data: List[Product]) -> None:
        for product in data:
            self._data.append(product)

    @property
    def data(self) -> List[Product]:
        return self._data.copy()
