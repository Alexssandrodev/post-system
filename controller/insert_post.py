from connection import ConnectionDb

class InsertPost(ConnectionDb):
    def insertPost(self, *args):
        try:
            sql = 'INSERT INTO insert_post (post, created_on) VALUES(%s, %s)'
            self.execute(sql, args)
            self.commit
        except Exception as e:
            print(f'Erro ao cadastrar post {e}')

    def selectAllPosts(self):
        try:
            post = 'SELECT * FROM insert_post'
            self.execute(post)
            data = self.fetchall()
            return data
        except Exception as e:
            print(f'Erro: ao retornar os posts {e}')