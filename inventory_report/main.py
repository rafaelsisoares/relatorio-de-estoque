from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    args = sys.argv
    if args[1].endswith('.csv'):
        inventory = InventoryRefactor(CsvImporter)
    elif args[1].endswith('.json'):
        inventory = InventoryRefactor(JsonImporter)
    else:
        inventory = InventoryRefactor(XmlImporter)
    if len(args) != 3:
        sys.stderr.write('Verifique os argumentos\n')
    else:
        sys.stdout.write(inventory.import_data(args[1], args[2]))
