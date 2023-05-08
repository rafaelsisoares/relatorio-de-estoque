from inventory_report.inventory.product import Product


product_id = 1
company = 'Organizações Tabajara'
product_name = 'Faca Guincho'
manufacturing_date = '2023-05-02'
expiration_date = '2026-05-02'
storage_info = 'em temperatura ambiente longe de fontes de umidade'
serial = '12345678'


def test_relatorio_produto():
    product = Product(
        product_id,
        product_name,
        company,
        manufacturing_date,
        expiration_date,
        serial,
        storage_info
    )

    assert product.__repr__() == (
        "O produto Faca Guincho "
        "fabricado em 2023-05-02 "
        "por Organizações Tabajara com validade "
        "até 2026-05-02 "
        "precisa ser armazenado em temperatura ambiente longe de fontes de umidade.")
