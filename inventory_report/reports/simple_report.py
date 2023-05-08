from datetime import date
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, products):
        today = date.today().strftime("%Y-%m-%d")
        oldest_product = min(
            product["data_de_fabricacao"] for product in products
        )
        next_expiration = min(
            product["data_de_validade"]
            for product in products
            if product["data_de_validade"] > today
        )
        all_companies = [product['nome_da_empresa'] for product in products]
        largest_stock_company = Counter(all_companies).most_common(1)[0]

        return (
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {next_expiration}\n"
            f"Empresa com mais produtos: {largest_stock_company[0]}"
        )
