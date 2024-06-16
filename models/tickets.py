from db import conn, cursor


class Ticket:

    TABLE_NAME = "tickets"

    def __init__(self):
        self.id = None

    @classmethod
    def create_table(cls):
        sql = f"""
          CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
        bus_id INTEGER NOT NULL REFERENCES buses(id)
        )
        """
        cursor.execute(sql)
        conn.commit()
        print("Tickets table created successfully")


Ticket.create_table()
