from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'super_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
PASSWORD = "1234"

# Simulação de banco de dados em memória
animais = []

# Página inicial
@app.route('/')
def index():
    return render_template('index.html', animais=animais)

# Página de contato
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        bicho = request.form['bicho']
        telefone = request.form['telefone']
        mensagem = request.form['mensagem']
        # Implementação para envio de email (exemplo de print no console)
        print(f"Email para abrigo@abrigo.com\nNome: {nome}\nBicho: {bicho}\nTelefone: {telefone}\nMensagem: {mensagem}")
        flash('Mensagem enviada com sucesso!')
        return redirect(url_for('index'))
    return render_template('contato.html')

# Página de login do admin
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            flash('Senha incorreta!')
    return render_template('login.html')

# Página de administração (protegida)
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        foto = request.files['foto']
        if foto:
            filename = secure_filename(foto.filename)
            foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            animais.append({'nome': nome, 'descricao': descricao, 'foto': filename})
            flash('Animal adicionado com sucesso!')
    return render_template('admin.html', animais=animais)

# Remover animal
@app.route('/remover/<int:index>')
def remover(index):
    if session.get('logged_in'):
        try:
            animais.pop(index)
            flash('Animal removido com sucesso!')
        except IndexError:
            flash('Animal não encontrado.')
        return redirect(url_for('admin'))
    return redirect(url_for('login'))

# Logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
