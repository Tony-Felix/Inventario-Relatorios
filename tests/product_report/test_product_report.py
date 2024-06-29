from inventory_report.product import Product


def test_product_report() -> None:
    produto = Product(
        "1234",
        "farinha",
        "Rei_da_farinha",
        "2024-06-09",
        "2024-09-09",
        "0123456789",
        "precisa ser armazenado em local protegido da luz",
    )

    assert (
        str(produto)
        == "The product 1234 - farinha with serial number 0123456789 manufactured on 2024-06-09 by the company Rei_da_farinha valid until 2024-09-09 must be stored according to the following instructions: precisa ser armazenado em local protegido da luz."
    )
