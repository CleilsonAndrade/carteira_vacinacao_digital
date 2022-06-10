# IMPORTS DOS MÓDULOS
import sqlite3
from urllib import response
from flask import Flask, render_template, request, url_for, flash, redirect

# DEFINIÇÃO DA VARIÁVEL GLOBAL
app = Flask(__name__)

# SENHA PARA CONEXÃO DO APLICATIVO AO BANCO DE DADOS
app.config['SECRET_KEY'] = '1cafa6e42aceef976ab7547b4a6a31e2'


# FUNÇÃO DE CONEXÃO COM O BANCO DE DADOS
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# REGISTRO INDEX - CADASTRO DE USUÁRIO
@app.route('/', methods=('GET', 'POST'))
def index():
    # VERIFICA O MÉTODO ENVIADO E RECUPERA AS INFORMAÇÕES DO FORMULÁRIO
    if request.method == 'POST':
        # ATRIBUI OS VALORES DOS CAMPOS A VARIÁVEIS
        usuario = request.form['usuario']
        email = request.form['email']
        idade = request.form['idade']
        sexo = request.form['sexo']

        # VALIDA O PREECHIMENTO DOS CAMPOS DE USUÁRIO E EMAIL, CASO NÃO PREECHIDOS RETORNA A PÁGINA DE REGISTRO COM MENSAGEM
        if usuario == '' or email == '':
            flash('Digite os dados!')
            return render_template('./autenticacao/index.html')
        else:
            # VALIDA A FAIXA ETÁRIA ENVIADA DO FORMULÁRIO E ENVIA OS DADOS PARA A ROTA DAS VACINAS CORRESPONDENTES A ELA
            # VALIDAÇÃO FAIXA ETÁRIA CRIANÇA
            if idade == '1':
                # ABRE A CONEXÃO COM O BANCO DE DADOS
                conn = get_db_connection()
                # INSERE OS DADOS DO FOMULÁRIO NA TABELA DE CRIANÇAS
                conn.execute('INSERT INTO criancas (usuario, email, sexo, idade) VALUES (?, ?, ?, ?)',
                             (usuario, email, sexo, idade))
                # GRAVA OS DADOS NO BANDO DE DADOS
                conn.commit()
                # FECHA A CONEXÃO COM O BANCO DE DADOS
                conn.close()
                # APÓS A GRAVAÇÃO O USUÁRIO É ENVIADO PARA A ROTA DAS CRIANÇAS O NOME DO USUÁRIO
                return redirect(url_for('crianca', usuario=usuario))
            # VALIDAÇÃO FAIXA ETÁRIA ADULTO
            elif idade == '2':
                # ABRE A CONEXÃO COM O BANCO DE DADOS
                conn = get_db_connection()
                # INSERE OS DADOS DO FOMULÁRIO NA TABELA DE ADULTOS
                conn.execute('INSERT INTO adultos (usuario, email, sexo, idade) VALUES (?, ?, ?, ?)',
                             (usuario, email, sexo, idade))
                # GRAVA OS DADOS NO BANDO DE DADOS
                conn.commit()
                # FECHA A CONEXÃO COM O BANCO DE DADOS
                conn.close()
                # APÓS A GRAVAÇÃO O USUÁRIO É ENVIADO PARA A ROTA DOS ADULTOS O NOME DO USUÁRIO
                return redirect(url_for('adulto', usuario=usuario))
            # VALIDAÇÃO FAIXA ETÁRIA IDOSO
            elif idade == '3':
                # ABRE A CONEXÃO COM O BANCO DE DADOS
                conn = get_db_connection()
                # INSERE OS DADOS DO FOMULÁRIO NA TABELA DE IDOSOS
                conn.execute('INSERT INTO idosos (usuario, email, sexo, idade) VALUES (?, ?, ?, ?)',
                             (usuario, email, sexo, idade))
                # GRAVA OS DADOS NO BANDO DE DADOS
                conn.commit()
                # FECHA A CONEXÃO COM O BANCO DE DADOS
                conn.close()
                # APÓS A GRAVAÇÃO O USUÁRIO É ENVIADO PARA A ROTA DOS IDOSOS O NOME DO USUÁRIO
                return redirect(url_for('idoso', usuario=usuario))
    # RENDERIZA A PÁGINA DE REGISTRO E LIMPA OS CAMPOS DE USUÁRIO E E-MAIL
    return render_template('./autenticacao/index.html', usuario='', email='')


# ROTA DE VACINAS DAS CRIANÇAS - CADASTRO DAS VACINAS DE CRIANÇAS
@app.route('/crianca', methods=('GET', 'POST'))
def crianca():
    # RECUPERA O NOME DO USUÁRIO ENVIADO POR PARÂMETRO
    usuario = request.args.get('usuario')

    # FORMATA O NOME DO USUÁRIO E ATRIBUI A UMA NOVA VARIÁVEL
    crianca = f"%{usuario}%"
    # ABRE A CONEXÃO COM O BANCO DE DADOS
    conn = get_db_connection()
    # SELECIONA TODOS OS DADOS DA TABELA DO BANCO DE DADOS ONDE O USUÁRIO É IGUAL A VARIÁVEL CRIANÇA
    crianca = conn.execute(
        'SELECT * FROM criancas WHERE usuario LIKE :resultado', {"resultado": usuario}).fetchone()
    # GRAVA OS DADOS NO BANDO DE DADOS
    conn.commit()
    # FECHA A CONEXÃO COM O BANCO DE DADOS
    conn.close()

    # VERIFICA O MÉTODO ENVIADO E RECUPERA AS INFORMAÇÕES DO FORMULÁRIO
    if request.method == 'POST':
        # VACINAS RECUPERADAS DO FORMULÁRIO QUE FORAM MARCADAS SE TOMOU OU NAO
        vacina1 = request.form['vacina1']
        vacina2 = request.form['vacina2']
        vacina3 = request.form['vacina3']
        vacina4 = request.form['vacina4']
        vacina5 = request.form['vacina5']
        vacina6 = request.form['vacina6']
        vacina7 = request.form['vacina7']
        vacina8 = request.form['vacina8']
        vacina9 = request.form['vacina9']
        vacina10 = request.form['vacina10']
        # ABRE A CONEXÃO COM O BANCO DE DADOS
        conn = get_db_connection()
        # ATUALIZA A TABELA DE CRIANÇAS DAS VACINAS VAZIAS NO BANCO DE DADOS COM AS DO FORMULÁRIO
        conn.execute('UPDATE criancas SET vacina1 = ?, vacina2 = ?, vacina3 = ?, vacina4 = ?, vacina5 = ?, vacina6 = ?, vacina7 = ?, vacina8 = ?, vacina9 = ?, vacina10 = ?' ' WHERE usuario = ?',
                     (vacina1, vacina2, vacina3, vacina4, vacina5, vacina6, vacina7, vacina8, vacina9, vacina10, usuario))
        # GRAVA OS DADOS NO BANDO DE DADOS
        conn.commit()
        # FECHA A CONEXÃO COM O BANCO DE DADOS
        conn.close()
        # MENSAGEM EXIBIDA DAS VACINAS INSERIDAS COM SUCESSO
        flash('Agradecemos pelo seu cadastro!')
        # USUÁRIO É REDIRECIONADO PARA TELA DE LOGIN EXBINDO A MENSAGEM
        return redirect(url_for('login'))
    # RENDERIZA A PÁGINA DAS VACINAS DE CRIANCAS COM OS DADOS RECUPERADOS DO USUÁRIO
    return render_template('vacinas/vacinas_cadastro/vacinas_criancas.html', usuario=crianca)


# ROTA DE VACINAS DOS ADULTOS - CADASTRO DAS VACINAS DE ADULTOS
@app.route('/adulto', methods=('GET', 'POST'))
def adulto():
    # RECUPERA O NOME DO USUÁRIO ENVIADO POR PARÂMETRO
    usuario = request.args.get('usuario')

    # FORMATA O NOME DO USUÁRIO E ATRIBUI A UMA NOVA VARIÁVEL
    adulto = f"%{usuario}%"
    # ABRE A CONEXÃO COM O BANCO DE DADOS
    conn = get_db_connection()
    # SELECIONA TODOS OS DADOS DA TABELA DO BANCO DE DADOS ONDE O USUÁRIO É IGUAL A VARIÁVEL ADULTO
    adulto = conn.execute(
        'SELECT * FROM adultos WHERE usuario LIKE :resultado', {"resultado": usuario}).fetchone()
    # GRAVA OS DADOS NO BANDO DE DADOS
    conn.commit()
    # FECHA A CONEXÃO COM O BANCO DE DADOS
    conn.close()

    # VERIFICA O MÉTODO ENVIADO E RECUPERA AS INFORMAÇÕES DO FORMULÁRIO
    if request.method == 'POST':
        # VACINAS RECUPERADAS DO FORMULÁRIO QUE FORAM MARCADAS SE TOMOU OU NAO
        vacina1 = request.form['vacina1']
        vacina2 = request.form['vacina2']
        vacina3 = request.form['vacina3']
        vacina4 = request.form['vacina4']
        vacina5 = request.form['vacina5']
        # ABRE A CONEXÃO COM O BANCO DE DADOS
        conn = get_db_connection()
        # ATUALIZA A TABELA DE CRIANÇAS DAS VACINAS VAZIAS NO BANCO DE DADOS COM AS DO FORMULÁRIO
        conn.execute('UPDATE adultos SET vacina1 = ?, vacina2 = ?, vacina3 = ?, vacina4 = ?, vacina5 = ?' ' WHERE usuario = ?',
                     (vacina1, vacina2, vacina3, vacina4, vacina5, usuario))
        # GRAVA OS DADOS NO BANDO DE DADOS
        conn.commit()
        # FECHA A CONEXÃO COM O BANCO DE DADOS
        conn.close()
        # MENSAGEM EXIBIDA DAS VACINAS INSERIDAS COM SUCESSO
        flash('Agradecemos pelo seu cadastro!')
        # USUÁRIO É REDIRECIONADO PARA TELA DE LOGIN EXBINDO A MENSAGEM
        return redirect(url_for('login'))
    # RENDERIZA A PÁGINA DAS VACINAS DE ADULTOS COM OS DADOS RECUPERADOS DO USUÁRIO
    return render_template('vacinas/vacinas_cadastro/vacinas_adultos.html', usuario=adulto)


# ROTA DE VACINAS DOS IDOSOS - CADASTRO DAS VACINAS DE IDOSOS
@app.route('/idoso', methods=('GET', 'POST'))
def idoso():
    # RECUPERA O NOME DO USUÁRIO ENVIADO POR PARÂMETRO
    usuario = request.args.get('usuario')

    # FORMATA O NOME DO USUÁRIO E ATRIBUI A UMA NOVA VARIÁVEL
    idoso = f"%{usuario}%"
    # ABRE A CONEXÃO COM O BANCO DE DADOS
    conn = get_db_connection()
    # SELECIONA TODOS OS DADOS DA TABELA DO BANCO DE DADOS ONDE O USUÁRIO É IGUAL A VARIÁVEL IDOSO
    idoso = conn.execute(
        'SELECT * FROM idosos WHERE usuario LIKE :resultado', {"resultado": usuario}).fetchone()
    # GRAVA OS DADOS NO BANDO DE DADOS
    conn.commit()
    # FECHA A CONEXÃO COM O BANCO DE DADOS
    conn.close()

    # VERIFICA O MÉTODO ENVIADO E RECUPERA AS INFORMAÇÕES DO FORMULÁRIO
    if request.method == 'POST':
        # VACINAS RECUPERADAS DO FORMULÁRIO QUE FORAM MARCADAS SE TOMOU OU NAO
        vacina1 = request.form['vacina1']
        vacina2 = request.form['vacina2']
        vacina3 = request.form['vacina3']
        vacina4 = request.form['vacina4']
        vacina5 = request.form['vacina5']
        # ABRE A CONEXÃO COM O BANCO DE DADOS
        conn = get_db_connection()
        # ATUALIZA A TABELA DE IDOSOS DAS VACINAS VAZIAS NO BANCO DE DADOS COM AS DO FORMULÁRIO
        conn.execute('UPDATE idosos SET vacina1 = ?, vacina2 = ?, vacina3 = ?, vacina4 = ?, vacina5 = ?' ' WHERE usuario = ?',
                     (vacina1, vacina2, vacina3, vacina4, vacina5, usuario))
        # GRAVA OS DADOS NO BANDO DE DADOS
        conn.commit()
        # FECHA A CONEXÃO COM O BANCO DE DADOS
        conn.close()
        # MENSAGEM EXIBIDA DAS VACINAS INSERIDAS COM SUCESSO
        flash('Agradecemos pelo seu cadastro!')
        # USUÁRIO É REDIRECIONADO PARA TELA DE LOGIN EXBINDO A MENSAGEM
        return redirect(url_for('login'))
    # RENDERIZA A PÁGINA DAS VACINAS DE IDOSOS COM OS DADOS RECUPERADOS DO USUÁRIO
    return render_template('vacinas/vacinas_cadastro/vacinas_idosos.html', usuario=idoso)


# LOGIN - ONDE É INSERIDO O USUÁRIO CRIADO PARA ACESSAR AS VACINAS CADASTRADAS
@ app.route('/login', methods=('GET', 'POST'))
def login():
    # VERIFICA O MÉTODO ENVIADO E RECUPERA AS INFORMAÇÕES DO FORMULÁRIO
    if request.method == 'POST':
        # ATRIBUI O VALOR DO CAMPO USUÁRIO UMA VARIÁVEL
        usuario = request.form['usuario']
        # VALIDA SE O CAMPO USUÁRIO DO FORMULÁRIO ESTÁ VAZIO
        if usuario == '':
            # SE O CAMPO ESTÁ VAZIO ENVIA UMA MENSAGEM
            flash('Digite os dados!')
            # RENDERIZA A PÁGINA DE LOGIN NOVAMENTE COM A MENSAGEM
            return render_template('./autenticacao/login.html')
        else:
            # FORMATA O NOME DO USUÁRIO E ATRIBUI A UMA NOVA VARIÁVEL
            usuario = f"%{usuario}%"
            # ABRE A CONEXÃO COM O BANCO DE DADOS
            conn = get_db_connection()

            # SELECIONA TUDO DA TABELA DE CRIANÇAS ONDE O USUÁRIO É IGUAL A NOVA VARIÁVEL USUÁRIO E SALVANDO OS DADOS NA MESMA
            crianca = conn.execute(
                'SELECT * FROM criancas WHERE usuario LIKE :resultado', {"resultado": usuario}).fetchone()

            # SELECIONA TUDO DA TABELA DE CRIANÇAS ONDE O USUÁRIO É IGUAL A NOVA VARIÁVEL USUÁRIO E SALVANDO OS DADOS NA MESMA
            adulto = conn.execute(
                'SELECT * FROM adultos WHERE usuario LIKE :resultado', {"resultado": usuario}).fetchone()

            # SELECIONA TUDO DA TABELA DE CRIANÇAS ONDE O USUÁRIO É IGUAL A NOVA VARIÁVEL USUÁRIO E SALVANDO OS DADOS NA MESMA
            idoso = conn.execute(
                'SELECT * FROM idosos WHERE usuario LIKE :resultado', {"resultado": usuario}).fetchone()

            # GRAVA OS DADOS NO BANDO DE DADOS
            conn.commit()
            # FECHA A CONEXÃO COM O BANCO DE DADOS
            conn.close()

            # VALIDA SE FOI ENCONTRADO O USUÁRIO
            if crianca != None:
                # SENDO VÁLIDO É ENVIADO Á PAGINA DE VACINAS CADASTRADAS ENVIANDO POR PARÂMETRO O VALOR DA VARIÁVEL
                return render_template('vacinas/vacinas_cadastradas/vacinas_cadastradas_criancas.html', usuario=crianca)
            # VALIDA SE FOI ENCONTRADO O USUÁRIO
            elif adulto != None:
                # SENDO VÁLIDO É ENVIADO Á PAGINA DE VACINAS CADASTRADAS ENVIANDO POR PARÂMETRO O VALOR DA VARIÁVEL
                return render_template('vacinas/vacinas_cadastradas/vacinas_cadastradas_adultos.html', usuario=adulto)
            # VALIDA SE FOI ENCONTRADO O USUÁRIO
            elif idoso != None:
                # SENDO VÁLIDO É ENVIADO Á PAGINA DE VACINAS CADASTRADAS ENVIANDO POR PARÂMETRO O VALOR DA VARIÁVEL
                return render_template('vacinas/vacinas_cadastradas/vacinas_cadastradas_idosos.html', usuario=idoso)
    # RENDERIZA A PÁGINA DE LOGIN
    return render_template('./autenticacao/login.html')


# UPDATE - ONDE O USUÁRIO ATUALIZA VIA FORMULÁRIO AS VACINAS TOMADAS
@ app.route('/update', methods=('GET', 'POST'))
def update():
    # VERIFICA O MÉTODO ENVIADO E RECUPERA AS INFORMAÇÕES DO FORMULÁRIO
    if request.method == 'POST':
        # RECUPERA O NOME DO USUÁRIO ENVIADO POR PARÂMETRO E IDADE
        usuario = request.args.get('usuario')
        idade = request.args.get('idade')
        # VERIFICA SE A FAIXA ETÁRIA É DE CRIANÇAS
        if idade == '1':
            # RECUPERA AS VACINAS DO FORMULÁRIO
            vacina1 = request.form['vacina1']
            vacina2 = request.form['vacina2']
            vacina3 = request.form['vacina3']
            vacina4 = request.form['vacina4']
            vacina5 = request.form['vacina5']
            vacina6 = request.form['vacina6']
            vacina7 = request.form['vacina7']
            vacina8 = request.form['vacina8']
            vacina9 = request.form['vacina9']
            vacina10 = request.form['vacina10']
            # ABRE A CONEXÃO COM O BANCO DE DADOS
            conn = get_db_connection()
            # ATUALIZA OS DADOS DAS VACINAS DA TABELA DE CRIANÇAS COM OS DADOS RECUPERADOS DO FORMULÁRIO
            conn.execute('UPDATE criancas SET vacina1 = ?, vacina2 = ?, vacina3 = ?, vacina4 = ?, vacina5 = ?, vacina6 = ?, vacina7 = ?, vacina8 = ?, vacina9 = ?, vacina10 = ?' ' WHERE usuario = ?',
                         (vacina1, vacina2, vacina3, vacina4, vacina5, vacina6, vacina7, vacina8, vacina9, vacina10, usuario))
            # GRAVA OS DADOS NO BANDO DE DADOS
            conn.commit()
            # FECHA A CONEXÃO COM O BANCO DE DADOS
            conn.close()
        # VERIFICA SE A FAIXA ETÁRIA É DE ADULTOS
        elif idade == '2':
            # RECUPERA AS VACINAS DO FORMULÁRIO
            vacina1 = request.form['vacina1']
            vacina2 = request.form['vacina2']
            vacina3 = request.form['vacina3']
            vacina4 = request.form['vacina4']
            vacina5 = request.form['vacina5']
            # ABRE A CONEXÃO COM O BANCO DE DADOS
            conn = get_db_connection()
            # ATUALIZA OS DADOS DAS VACINAS DA TABELA DE ADULTOS COM OS DADOS RECUPERADOS DO FORMULÁRIO
            conn.execute('UPDATE adultos SET vacina1 = ?, vacina2 = ?, vacina3 = ?, vacina4 = ?, vacina5 = ?' ' WHERE usuario = ?',
                         (vacina1, vacina2, vacina3, vacina4, vacina5, usuario))
            # GRAVA OS DADOS NO BANDO DE DADOS
            conn.commit()
            # FECHA A CONEXÃO COM O BANCO DE DADOS
            conn.close()
        # VERIFICA SE A FAIXA ETÁRIA É DE IDOSOS
        elif idade == '3':
            # RECUPERA AS VACINAS DO FORMULÁRIO
            vacina1 = request.form['vacina1']
            vacina2 = request.form['vacina2']
            vacina3 = request.form['vacina3']
            vacina4 = request.form['vacina4']
            vacina5 = request.form['vacina5']
            # ABRE A CONEXÃO COM O BANCO DE DADOS
            conn = get_db_connection()
            # ATUALIZA OS DADOS DAS VACINAS DA TABELA DE IDOSOS COM OS DADOS RECUPERADOS DO FORMULÁRIO
            conn.execute('UPDATE idosos SET vacina1 = ?, vacina2 = ?, vacina3 = ?, vacina4 = ?, vacina5 = ?' ' WHERE usuario = ?',
                         (vacina1, vacina2, vacina3, vacina4, vacina5, usuario))
            # GRAVA OS DADOS NO BANDO DE DADOS
            conn.commit()
            # FECHA A CONEXÃO COM O BANCO DE DADOS
            conn.close()
    # ENVIA UMA MENSAGEM DE VACINAS ATUALIZADAS COM SUCESSO
    flash('Seus dados foram atualizados!')
    # RETORNA A ROTA DE LOGIN EXIBINDO A MENSAGEM
    return redirect(url_for('login'))


# PÁGINA PARA O ERRO DE 404 (PÁGINA NÃO ENCONTRADA)
# FUNÇÃO DE ERRO ONDE É PASSADO POR PARÂMETRO QUAL O ERRO ASER TRATATDO
@ app.errorhandler(404)
def page_not_found(e):
    # SENDO A PÁGINA DE ERRO REFERENTE AO PARÂMETRO RENDERIZA A PÁGINA DE ERRO
    return render_template('error404/index.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
