import json

from base_server import BaseHttpServer


class JsonServer(BaseHttpServer):
    port = 5002
    content_type = "application/json"
    dateformat = "%Y-%m-%d %H:%M"
    server_name = "json_server"

    def get_response(self, formatted_datetime, number):
        return json.dumps({"data": str(number), "date": formatted_datetime})


def main():
    JsonServer().run()


if __name__ == "__main__":
    main()
