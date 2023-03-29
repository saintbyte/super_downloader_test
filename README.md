# Super donwloader project


# Servers
### Start
В директории servers
запустить файлы:
*  xml_server.py
*  json_server.py
*  text_server.py

Командой например: ```python3 text_server.py```

### Ports
| Server|   Port 	|
|---	|---	|
|  xml_server 	|  5001 |
|  json_server 	|  5002 |
|  text_server 	|  5003 |

## Client

### Run
```cd client & python3 main.py```

### Настройка
Настройка производиться через файл ```.env``` cм .env-example

| Параметр       | Описание 	                                         | По умолчанию                                                      |
|----------------|----------------------------------------------------|-------------------------------------------------------------------|
| URL_SERVERS    | Адреса серверов с исходными данным , через запятую | http://localhost:5001, http://localhost:5002, http://localhost:5003 |
| THRESHOLD_URL  | Адрес уведомления о достижение порога              | http://localhost:5004                                             |
| DB_FILE        | Файл базы sqllite                                  | "db.sqllite3                                                      |
| THRESHOLD      | Порог                                              | 1000                                                              |
| MAX_ERROR_CNT  | Максимальное количество ошибок скачивание до прекращения| 100 |
