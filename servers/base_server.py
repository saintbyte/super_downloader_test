import datetime
import os
import random
import typing as t

from flask import Flask
from flask import make_response
from flask import render_template_string


class BaseHttpServer(Flask):
    def get_response(self, formatted_datetime, number):
        return render_template_string(
            self.template, formatted_datetime=formatted_datetime, number=number
        )

    def index(self):
        response = make_response(
            self.get_response(
                self.get_formated_current_time(), self.get_random_float()
            ),
            200,
        )
        response.headers["Content-Type"] = self.content_type
        return response

    def __init__(
        self,
        import_name: t.Optional[str] = None,
        static_url_path: t.Optional[str] = None,
        static_folder: t.Optional[t.Union[str, os.PathLike]] = "static",
        static_host: t.Optional[str] = None,
        host_matching: bool = False,
        subdomain_matching: bool = False,
        template_folder: t.Optional[t.Union[str, os.PathLike]] = "templates",
        instance_path: t.Optional[str] = None,
        instance_relative_config: bool = False,
        root_path: t.Optional[str] = None,
    ):
        if import_name is None:
            import_name = self.server_name
        super().__init__(
            import_name,
            static_url_path,
            static_folder,
            static_host,
            host_matching,
            subdomain_matching,
            template_folder,
            instance_path,
            instance_relative_config,
            root_path,
        )
        self.add_url_rule("/", view_func=self.index)

    def get_random_float(self):
        return random.uniform(0.0, 10.0)

    def get_formated_current_time(self):
        return datetime.datetime.now().strftime(self.dateformat)

    def run(self, **options: t.Any) -> None:
        super().run("", self.port, True, True, **options)
