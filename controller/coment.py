from connection import ConnectionDb

class Coment(ConnectionDb):

    def inserComent(self, *args):
        try:
            sql = 'INSERT INTO coment (text, autor, create_on, id_post) VALUES(%s, %s, %s, %s)'
            self.execute(sql, args)
            self.commit
        except Exception as e:
            print(f'Erro: ao postar comentário {e}')

    def selectAllComents(self):
        try:
            sql = 'SELECT * FROM coment'
            self.execute(sql)
            data = self.fetchall()
            return data
        except Exception as e:
            print(f'Erro: ao retornar comentários')