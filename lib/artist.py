from config import CONN, CURSOR

class Artist:

    def __init__(self, name, age):
        self.id = None
        self.name = name
        self.age = age

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS artists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
            )
        """
        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO artists (name, age)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.age))
        CONN.commit()  
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, age):
        artist = cls(name, age) 
        artist.save() 
        return artist  
