from connection import ConnectionDb

class RegisterUser(ConnectionDb):
    def insertRegister(self, *args):
        try:
            sql = 'INSERT INTO register_user (nome, email, senha) VALUES(%s, %s, %s)'
            self.execute(sql, args)
            self.commit
        except Exception as e:
            print(f'Erro ao cadastrar usuário {e}')

    def selectUserId(self):
        try:
            user_id = 'SELECT * FROM register_user'
            self.execute(user_id)
            data = self.fetchall()
            return data
        except Exception as e:
            print(f'Erro: ao retornar os usuários {e}')

