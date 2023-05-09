import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        ext = path.split(".")[-1]
        if ext != "xml":
            raise ValueError("Arquivo inválido")

        tree = ET.parse(path)
        root = tree.getroot()
        return [
            dict((item.tag, item.text) for item in record) for record in root
        ]
