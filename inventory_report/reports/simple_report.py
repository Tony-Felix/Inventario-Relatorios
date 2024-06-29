from inventory_report.inventory import Inventory


class SimpleReport:
    def __init__(self) -> None:
        self.data = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.data.append(inventory)

    def generate(self) -> str:
        oldest_manufacturing = "7000-12-31"
        closest_expiration = "7000-12-31"
        largest_inventory = dict()

        for invent in self.data:
            for product in invent.data:
                if product.manufacturing_date < oldest_manufacturing:
                    oldest_manufacturing = product.manufacturing_date

                if product.expiration_date < closest_expiration:
                    closest_expiration = product.expiration_date

                largest_inventory[product.company_name] = (
                    largest_inventory.get(product.company_name, 0) + 1
                )

        company_name = max(
            largest_inventory, key=lambda x: largest_inventory[x]
        )

        return (
            f"Oldest manufacturing date: {oldest_manufacturing}"
            f"Closest expiration date: {closest_expiration}"
            f"Company with the largest inventory: {company_name}"
        )
