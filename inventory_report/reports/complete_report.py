from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, products):
        companies_stock = Counter([
            product['nome_da_empresa'] for product in products
            ]).most_common()
        report = super().generate(products)
        report += '\nProdutos estocados por empresa:\n'
        for company, stock in companies_stock:
            report += f"- {company}: {stock}\n"
        return report
