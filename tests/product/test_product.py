from inventory_report.product import Product


def test_create_product() -> None:
    produto = Product(
        "1234",
        "farinha",
        "Rei_da_farinha",
        "2024-06-09",
        "2024-09-09",
        "0123456789",
        "saida_de_emergencia_ao_centro",
    )
    assert produto.id == "1234"
    assert produto.product_name == "farinha"
    assert produto.company_name == "Rei_da_farinha"
    assert produto.manufacturing_date == "2024-06-09"
    assert produto.expiration_date == "2024-09-09"
    assert produto.serial_number == "0123456789"
    assert produto.storage_instructions == "saida_de_emergencia_ao_centro"
