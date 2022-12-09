from connection import ConnectionDb

class RegisterUser(ConnectionDb):
    def insertRegister(self, *args):
        try:
            sql = 'INSERT INTO register_user (nome, email, senha, created_on, last_login) VALUES(%s, %s, %s, %s, %s)'
            self.execute(sql, args)
            self.commit
        except Exception as e:
            print(f'Erro ao cadastrar usuário {e}')

    def selectUsers(self):
        try:
            user_id = 'SELECT * FROM register_user'
            self.execute(user_id)
            data = self.fetchall()
            return data
        except Exception as e:
            print(f'Erro: ao retornar os usuários {e}')

    def getUserId(self):
        all_users = self.selectUsers()
        for users in all_users:
            user_id = users[0]

        return user_id


        

