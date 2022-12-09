from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from connection import ConnectionDb
from controller.insert_post import InsertPost
from controller.register_user import RegisterUser
from controller.coment import Coment
from datetime import datetime

conn = ConnectionDb()
date_system = datetime.now()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'webdesign'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():
    post = InsertPost()
    all_posts = post.selectAllPosts()

    client = RegisterUser()
    user_client = client.selectUsers()
    
    coment = Coment()
    post_coment = coment.selectAllComents()

    if not session.get('user'):
        return redirect(url_for('login'))
    
    return render_template('index.html', posts = all_posts, users = user_client, coment = post_coment)

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        insert = InsertPost()
        post = request.form['post']
        autor = session.get('name')
        if post == '':
            flash('O campo post é requerido.', category='error')
        else:
            insert.insertPost(post, autor, date_system)
            
        flash('post feito com sucesso!.', category='success')
        return redirect(url_for('index'))

@app.route('/coment/<id_post>', methods=['POST'])
def coment(id_post):
    if request.method == 'POST':
        coment = Coment()
        text = request.form['coment']
        autor = session.get('name')

        coment.inserComent(text, autor, date_system, id_post)
        flash('Comentário adicionado', category='success')

        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        new_user = RegisterUser()
        last_login = datetime.now()

        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        _hashed_password = generate_password_hash(senha)

        if nome == '':
            flash('O campo nome é obrigatório', category='error')
        elif len(email) < 5:
            flash('Email incorreto', category='error')
        elif len(senha) <= 5:
            flash('A senha é obrigatória, precisa ter 5 ou mais caracters', category='error') 
        else:
            new_user.insertRegister(nome, email, _hashed_password, date_system, last_login)
            flash('Cadastro realizado com sucesso', category='success')
            return redirect(url_for('register'))
    return render_template('register.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = RegisterUser()
        email = request.form['email']
        senha = request.form['senha']

        user_login = user.selectUsers()
        
        for users in user_login:
            if users[2] != email:
                flash('Este email não existe na base de dados', category='error')
            else:
                if users[2]:
                    if check_password_hash(users[3], senha):
                        session['user'] = users[2]
                        session['name'] = users[1]
                        flash('Login feito com sucesso!', category='success')
                        return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == ('__main__'):
    app.run(debug=True)