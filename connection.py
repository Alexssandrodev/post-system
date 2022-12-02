import psycopg2 as db

class ConnectionDb:
    def __init__(self):
        self.DB_NAME = 'infosolutions.db'
        self.DB_USER = 'postgres'
        self.DB_PASS = 'webdesign'
        self.DB_PORT = 5432
        self.DB_HOST = 'localhost'

        self.conn = db.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS, port=self.DB_PORT)
        self.cur = self.conn.cursor()

    @property
    def cursor(self):
        return self.cur

    @property
    def commit(self):
        self.conn.commit()
    
    def fetchall(self):
        return self.cur.fetchall()

    def execute(self, sql, params = None):
        self.cursor.execute(sql, params or ())

    def query(self, sql, params = None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()


        
        
       