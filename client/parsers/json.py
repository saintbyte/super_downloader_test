import json
from datetime import datetime


class ParserJSON:
    datetime_format = "%Y-%m-%d %H:%M"

    def __init__(self, content):
        self.content = content

    def parse(self):
        data = json.loads(self.content)
        dt = datetime.strptime(data["date"], self.datetime_format)
        number = float(data["data"])
        return number, dt
