from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

GREEN = '\033[32m'
BLUE = '\033[36m'
RED = '\033[31m'
END = '\033[0m'
PRODUCTS = [
        {
            "id": 1,
            "nome_do_produto": "CADEIRA",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-04-04",
            "data_de_validade": "2023-12-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        }
    ]


def test_decorar_relatorio():
    phrases = [
        f"{GREEN}Data de fabricação mais antiga:{END} {BLUE}2022-04-04{END}",
        f"{GREEN}Data de validade mais próxima:{END} {BLUE}2023-12-09{END}",
        f"{GREEN}Empresa com mais produtos:{END} {RED}Forces of Nature{END}"
    ]
    report = ColoredReport(SimpleReport).generate(PRODUCTS)
    print(report)
    for phrase in phrases:
        assert phrase in report
