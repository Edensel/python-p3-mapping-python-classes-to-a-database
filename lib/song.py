from config import CONN, CURSOR

class Song:
    all = []  # Define `all` as a class attribute
    
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()  
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, album):
        song = cls(name, album) 
        song.save() 
        return song  
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM songs
        """

        all = CURSOR.execute(sql).fetchall()

        cls.all = [cls.new_from_db(row) for row in all]  # Populate Song.all list with Song objects

    @classmethod
    def new_from_db(cls, row):
        id, name, album = row
        song = cls(name, album)
        song.id = id
        return song
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM songs
            WHERE name = ?
            LIMIT 1
        """

        song = CURSOR.execute(sql, (name,)).fetchone()

        return cls.new_from_db(song)    
    
    
    



