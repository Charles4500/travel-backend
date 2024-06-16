from db import conn, cursor


class Ticket:

    TABLE_NAME = "tickets"

    def __init__(self, location_from, location_to, price, customer_id):
        self.id = None
        self.location_from = location_from
        self.location_to = location_to
        self.price = price
        self.customer_id = customer_id

    def save(self):
        sql = f"""
         INSERT INTO {self.TABLE_NAME} (location_from,location_to,price,customer_id) VALUES(?, ?, ?, ?)
        """
        cursor.execute(sql)
        conn.commit()
        self.id = cursor.lastrowid

        return self

    @classmethod
    def create_table(cls):
        sql = f"""
          CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          location_from TEXT NOT NULL,
          location_to TEXT NOT NULL,
          price INTEGER NOT NULL,
          bus_id INTEGER NOT NULL REFERENCES buses (id),
          customer_id INTEGER NOT NULL REFERENCES customers (id),
        )
        """
        cursor.execute(sql)
        conn.commit()
        print("Tickets table created successfully")


Ticket.create_table()
