from base_server import BaseHttpServer


class XmlServer(BaseHttpServer):
    port = 5003
    content_type = "text/plain"
    dateformat = "%s"
    server_name = "text_server"
    template = """{{formatted_datetime}} {{number}}"""


def main():
    XmlServer().run()


if __name__ == "__main__":
    main()
