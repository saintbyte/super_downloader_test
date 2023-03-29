import xml.etree.ElementTree as ElementTree
from datetime import datetime


class ParserXML:
    datetime_format = "%d-%m-%Y %H:%M"

    def __init__(self, content):
        self.content = content

    def parse(self):
        root = ElementTree.fromstring(self.content)
        dt = datetime.strptime(root.find("date").text, self.datetime_format)
        number = float(root.find("data").text)
        return number, dt
