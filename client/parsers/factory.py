from requests import Response

from .json import ParserJSON
from .text import ParserText
from .xml import ParserXML


class ParserFactory:
    def __new__(cls, response: Response, *args, **kwargs):
        content_type = response.headers["Content-Type"]
        if content_type == "text/xml":
            return ParserXML(response.text)
        if content_type == "application/json":
            return ParserJSON(response.text)
        if content_type == "text/plain":
            return ParserText(response.text)
        raise NotImplementedError
