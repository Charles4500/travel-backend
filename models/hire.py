from db import cursor, conn


class Hire:

    TABLE_NAME = "hire"

    def __init__(self, name, car_brand, image, hire_fee, date_hire):
        self.id = None
        self.name = name
        self.car_brand = car_brand
        self.image = image
        self.hire_fee = hire_fee
        self.date_hire = date_hire

    def save(self):
        sql = f"""
        INSERT INTO {self.TABLE_NAME} (name,car_brand,image,hire_fee,date_hire)
        VALUES  (?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.car_brand,
                       self.image, self.hire_fee, self.date_hire))
        conn.commit()
        self.id = cursor.lastrowid

        return self

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "car_brand": self.car_brand,
            "image": self.image,
            "hire_fee": self.hire_fee,
            "date_hire": self.date_hire
        }

    @classmethod
    def create_table(cls):
        sql = f"""
        CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
            id  INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            car_brand TEXT NOT NULL,
            image VARCHAR NOT NULL,
            hire_fee INTEGER NOT NULL,
            date_hire TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(sql)
        conn.commit()
        print("Hire out table created")


Hire.create_table()
