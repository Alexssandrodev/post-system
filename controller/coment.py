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

    def deleteComent(self, coment_id):
        try:
            sql_d = 'DELETE FROM coment WHERE id = {0}'.format(coment_id)
            self.execute(sql_d)
            self.commit
        except Exception as e:
            print(f'Erro: ao deletar post: {e}')