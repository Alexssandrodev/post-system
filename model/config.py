import psycopg2 as db

class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                'user': 'postgres',
                'password': 'webdesign',
                'host': 'localhost',
                'port': '5432',
                'database': 'infosolutions.db'
            }
        }

class Connection(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect(**self.config['postgres'])
            self.cur = self.conn.cursor()
        except Exception as e:
            print('Erro na conexão', e)
            exit(1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur

    def commit(self):
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

class Clientes(Connection):
    def __init__(self):
        Connection.__init__(self)


    def insert(self, *args):
        try:
            sql = 'INSERT INTO contact (nome, email, mensagem) VALUES(%s, %s, %s)'
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print('Erro ao inserir', e)

    def insert_post(self, *args):
        try:
            sql = 'INSERT INTO post (post) VALUES(%s)'
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print('Erro ao cadastrar', e)

    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM students WHERE id = {id}"
            if not self.query(sql_s):
                return 'Registro não encontrado'
            sql_d = f"DELETE FROM students WHERE id = {id}"
            self.execute(sql_d)
            self.commit()
        except Exception as e:
            print('Erro ao deletar', e)

    
    def update(self, id, *args):
        try:
            sql = f"UPDATE students SET fname = %s, lname = %s, email = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print('Erro ao atualizar', e)

    def search(self, *args, type_s="name"):
        sql = "SELECT * FROM students WHERE name LIKE %%s%"
        if type_s == "id":
            sql = "SELECT * FROM students WHERE id = %s"
        data = self.query(sql, args)
        if data:
            return data
        return "registro não encontrado"