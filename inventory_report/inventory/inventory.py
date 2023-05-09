import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def csv_reader(path):
        with open(path, mode="r", encoding="utf-8") as file:
            data = csv.DictReader(file, delimiter=",")
            return list(data)

    @staticmethod
    def json_reader(path):
        with open(path, mode="r") as file:
            data = json.load(file)
            return data

    @staticmethod
    def xml_reader(path):
        tree = ET.parse(path)
        root = tree.getroot()
        return [
            dict((item.tag, item.text) for item in record) for record in root
        ]

    @staticmethod
    def import_data(path, type):
        ext = path.split(".")[-1]
        if ext == "csv":
            imported_data = Inventory.csv_reader(path)
        elif ext == "json":
            imported_data = Inventory.json_reader(path)
        elif ext == "xml":
            imported_data = Inventory.xml_reader(path)
        else:
            raise TypeError("Arquivo com formato inválido")

        if type == "simples":
            return SimpleReport.generate(imported_data)
        else:
            return CompleteReport.generate(imported_data)
