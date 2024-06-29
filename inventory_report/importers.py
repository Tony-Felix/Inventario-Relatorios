from abc import ABC, abstractmethod
import json
from inventory_report.product import Product
from typing import Dict, List, Type


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def import_data(self) -> list[Product]:
        if self.path.endswith(".json"):
            result = []
            with open(self.path, "r") as file:
                data = json.load(file)
                for produto in data:
                    instancia_product = Product(**produto)
                    result.append(instancia_product)
            return result


class CsvImporter(Importer):
    pass
    # def __init__(self, path: str) -> None:
    #     super().__init__(path)

    # def import_data(self) -> list[Product]:
    #     with open(self.path, "r") as file:
    #         data = csv.load(file)
    #         return data


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
