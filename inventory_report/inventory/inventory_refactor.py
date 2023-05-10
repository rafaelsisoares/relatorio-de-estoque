from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []
        self.report = ''

    def import_data(self, path, type):
        products = self.importer.import_data(path)
        self.data += products
        if type == "simples":
            self.report = SimpleReport().generate(products)
        else:
            self.report = CompleteReport().generate(products)

        return self.report

    def __iter__(self):
        return InventoryIterator(self.data)
