import sqlite3


class SqlliteRepository:

    _default_ext = ".sqllite3"
    _allowed_sqllite_file_ext = [".sqllite", ".db", ".sqllite3"]
    _data_db_table = "data_table"

    def _normalization_db_filename(self, db_file: str) -> str:
        has_allowed_ext: bool = False
        for ext in self._allowed_sqllite_file_ext:
            if db_file.endswith(ext.lower()):
                has_allowed_ext = True
                break
        if not has_allowed_ext:
            db_file = f"{db_file}{self._default_ext}"
        return db_file

    def __init__(self, db_file: str):
        db_file = self._normalization_db_filename(db_file)
        try:
            self._connection: sqlite3.Connection = sqlite3.connect(db_file)
        except sqlite3.Error as e:
            if not self._connection:
                return
            self._connection.close()
            print(f"Error on open database file: {e}")
            quit()
        self._create_db()

    def _create_db(self):
        cursor = self._connection.cursor()
        sql_create_db: str = f"""CREATE TABLE IF NOT EXISTS {self._data_db_table}
         (
             number REAL,
             date DATE UNIQUE
         );
        """
        cursor.execute(sql_create_db)
        sql_index_db: str = f"CREATE INDEX IF NOT EXISTS {self._data_db_table}_date_index on {self._data_db_table}(date);"
        cursor.execute(sql_index_db)
        cursor.close()

    def store(self, number, date):
        cursor = self._connection.cursor()
        try:
            cursor.execute(
                f"INSERT INTO {self._data_db_table} (number, date) VALUES (?, ?)",
                (number, date),
            )
            self._connection.commit()
            cursor.close()
            return True
        except sqlite3.IntegrityError:
            cursor.close()
            return False

    def get_sum_by_date(self, date):
        cursor = self._connection.cursor()
        cursor.execute(
            f"SELECT SUM(number) FROM {self._data_db_table} WHERE date(date) = date(?)",
            (date,),
        )
        total = cursor.fetchone()[0]
        cursor.close()
        return total

    def close(self):
        if self._connection:
            self._connection.close()
