from config import CONN, CURSOR

class Artist:

    all = []

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
    
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM artists
        """

        all = CURSOR.execute(sql).fetchall()

        cls.all = [cls.new_from_db(row) for row in all]  

    @classmethod
    def new_from_db(cls, row):
        id, name, age = row
        artist = cls(name, age)
        artist.id = id
        return artist
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM artists
            WHERE name = ?
            LIMIT 1
        """

        artist = CURSOR.execute(sql, (name,)).fetchone()

        return cls.new_from_db(artist)