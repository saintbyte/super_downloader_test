from datetime import datetime


class ParserText:
    datetime_format = "%Y-%m-%d %H:%M:%S"

    def __init__(self, content):
        self.content = content

    def parse(self):
        parts = self.content.split(" ")
        number = float(parts[1])
        dt = datetime.fromtimestamp(int(parts[0]))
        return number, dt
