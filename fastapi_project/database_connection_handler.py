import psycopg2
from dataclasses import dataclass
import psycopg2.extras

@dataclass
class DbConnectionHandler:
    database: str = "postgres"
    user: str = "postgres"
    password: str = "postgres"
    host: str = "localhost"
    port: int = 5432

    def connect_to_db(self):
        conn = psycopg2.connect(database=self.database,
                                user=self.user,
                                password=self.password,
                                host=self.host,
                                port=self.port)
        return conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor), conn


if __name__ == "__main__":

    db = DbConnectionHandler()
    cursor = db.connect_to_db()
    cursor.execute("SELECT * FROM notes")
    records = cursor.fetchall()
    print(records)
