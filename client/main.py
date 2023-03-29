import os
from datetime import datetime

import requests
from dotenv import load_dotenv
from parsers.factory import ParserFactory
from repositories.sqllite import SqlliteRepository
from requests.exceptions import ConnectionError
from requests.exceptions import RequestException
from urllib3.exceptions import NewConnectionError

load_dotenv()


def download_url(url: str):
    response = requests.get(url)
    return response


def send_threshold_notify(date):
    threshold_url = os.environ.get("THRESHOLD_URL")
    try:
        requests.post(threshold_url, data={"event_time": date})
    except (
        ConnectionError,
        RequestException,
        NewConnectionError,
        ConnectionRefusedError,
    ) as e:
        print(f"Threshold notify connection Error: {e}")
    except Exception as e:
        print(f"Threshold notify  Error: {e}")
        quit()


def main():
    threshold = int(os.environ.get("THRESHOLD"))
    max_error_cnt = int(os.environ.get("MAX_ERROR_CNT"))
    storage = SqlliteRepository(os.environ.get("DB_FILE"))
    url_list = [url.strip() for url in os.environ.get("URL_SERVERS").split(",")]
    should_end: bool = False
    error_cnt = 0
    while not should_end:
        for url in url_list:
            if error_cnt > max_error_cnt:
                should_end = True
            try:
                resp = download_url(url)
                (number, dt) = ParserFactory(resp).parse()
            except (
                ConnectionError,
                RequestException,
                NewConnectionError,
                ConnectionRefusedError,
            ) as e:
                print(f"Connection Error: {e}")
                error_cnt = error_cnt + 1
                continue
            except Exception as e:
                print(f"Error: {e}")
                quit()
            storage.store(number, dt)
            current_date = datetime.now()
            current_sum = storage.get_sum_by_date(current_date)
            if current_sum > threshold:
                print(f"Reached: {current_sum}")
                send_threshold_notify(current_date)
                should_end = True


if __name__ == "__main__":
    main()
