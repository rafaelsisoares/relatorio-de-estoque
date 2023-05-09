import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        ext = path.split(".")[-1]
        if ext != "csv":
            raise ValueError("Arquivo inválido")

        with open(path, mode="r", encoding="utf-8") as file:
            data = csv.DictReader(file, delimiter=",")
            return list(data)
