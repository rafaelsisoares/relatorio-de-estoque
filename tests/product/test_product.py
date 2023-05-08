from inventory_report.inventory.product import Product

product_id = 1
company = 'Organizações Tabajara'
product_name = 'Faca Guincho'
manufacturing_date = '2023-05-02'
expiration_date = '2026-05-02'
storage_info = 'Armazenar em temperatura ambiente longe de fontes de umidade.'
serial = '12345678'


def test_cria_produto():
    product = Product(
        product_id,
        product_name,
        company,
        manufacturing_date,
        expiration_date,
        serial,
        storage_info
    )

    assert product.id == product_id
    assert product.nome_do_produto == product_name
    assert product.nome_da_empresa == company
    assert product.data_de_fabricacao == manufacturing_date
    assert product.data_de_validade == expiration_date
    assert product.instrucoes_de_armazenamento == storage_info
    assert product.numero_de_serie == serial
