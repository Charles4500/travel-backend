from db import cursor, conn


class Buses:

    TABLE_BUSES = "buses"

    def __init__(self, name, location_from, location_to, passengers, price):
        self.id = None
        self.name = name
        self.location_from = location_from
        self.location_to = location_to
        self.passengers = passengers
        self.price = price

    def save(self):
        sql = f"""
          INSERT INTO {self.TABLE_BUSES} (name,car_brand,image,hire_fee,date_hire)
          VALUES  (?, ?, ?, ?, ?)
          """
        cursor.execute(sql, (self.name, self.location_from,
                             self.location_to, self.passengers, self.price))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def create_table(cls):
        sql = f"""
          CREATE TABLE IF NOT EXISTS {cls.TABLE_BUSES} (
              id  INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              location_from TEXT NOT NULL,
              location_to VARCHAR NOT NULL,
              passengers INTEGER NOT NULL,
              price INTEGER NOT NULL
          )
          """
        cursor.execute(sql)
        conn.commit()
        print("Hire out table created")


Buses.create_table()
