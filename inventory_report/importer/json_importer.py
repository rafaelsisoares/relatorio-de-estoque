import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        ext = path.split(".")[-1]
        if ext != "json":
            raise ValueError("Arquivo inválido")

        with open(path, mode="r") as file:
            return json.load(file)
