from crypt import methods
from flask import Flask, render_template, request, session, logging, redirect, url_for, flash
from model.config import Clientes, Connection
import psycopg2 as db
from connection import ConnectionDb
from controller.insert_post import InsertPost
from controller.register_user import RegisterUser
from datetime import datetime

conn = ConnectionDb()

date_system = datetime.now()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'webdesign'

@app.route('/')
def index():
    post = InsertPost()
    all_posts = post.selectAllPosts()

    client = RegisterUser()
    user_client = client.selectUserId()
    
    return render_template('index.html', posts = all_posts, user_nome = user_client)

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        insert = InsertPost()
        post = request.form['post']
        if post == '':
            flash('O campo post é requerido.', category='error')
        else:
            insert.insertPost(post, date_system)
            flash('post feito com sucesso!.', category='success')

        return redirect(url_for('index'))

@app.route('/user/<id>')
def user(id):
    data = conn.query('SELECT * FROM register_user WHERE user_id = %s', id)
    return render_template('user.html', data = data)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        new_user = RegisterUser()
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        if nome == '':
            flash('O campo nome é obrigatório', category='error')
        elif len(email) < 5:
            flash('Email incorreto', category='error')
        elif len(senha) <= 5:
            flash('A senha é obrigatória, precisa ter 5 ou mais caracters', category='error') 
        else:
            new_user.insertRegister(nome, email, senha)
            flash('Cadastro realizado com sucesso', category='success')
            return redirect(url_for('register'))
    return render_template('register.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        account = conn.query('SELECT email FROM register_user')
        password = conn.query('SELECT senha FROM register_user')

        for user in account:
            for i in user:
                if i == email:
                    for pass_word in password:
                        for word in pass_word:
                            if word == senha:
                                session['user'] = i
                                return redirect(url_for('index'))
                            if word != senha:
                                flash('Senha incorreta', category='error')
                if i != email:
                    flash('Email incorreto', category='error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employe(id):
    cliente = Connection()
    sql = "SELECT * FROM post"
    data = cliente.query(sql)
    cliente.commit()
    return render_template('edit.html', student = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_student(id):
    cliente = Clientes()
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']

        cliente.update(id, fname, lname, email)

    return redirect(url_for('index'))

@app.route('/delete/<id>', methods = ['POST', 'GET'])
def delete_student(id):
    cliente = Clientes()
    cliente.delete(id)

    return redirect(url_for('index'))



@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == ('__main__'):
    app.run(debug=True)