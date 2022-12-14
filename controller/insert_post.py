from connection import ConnectionDb

class InsertPost(ConnectionDb):
    def insertPost(self, *args):
        try:
            sql = 'INSERT INTO insert_post (post, autor, created_on) VALUES(%s, %s, %s)'
            self.execute(sql, args)
            self.commit
        except Exception as e:
            print(f'Erro ao cadastrar post {e}')

    def selectAllPosts(self):
        try:
            post = 'SELECT * FROM insert_post ORDER BY id DESC'
            self.execute(post)
            data = self.fetchall()
            return data
        except Exception as e:
            print(f'Erro: ao retornar os posts {e}')

    