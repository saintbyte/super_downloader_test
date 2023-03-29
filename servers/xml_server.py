from base_server import BaseHttpServer


class XmlServer(BaseHttpServer):
    port = 5001
    content_type = "text/xml"
    dateformat = "%d-%m-%Y %H:%M"
    server_name = "xml_server"
    template = (
        """<?xml version="1.0" encoding="UTF-8" ?>"""
        """<root><date>{{formatted_datetime}}</date><data>{{number}}</data></root>"""
    )


def main():
    XmlServer().run()


if __name__ == "__main__":
    main()
