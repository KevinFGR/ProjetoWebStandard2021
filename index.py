from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__,static_folder="static")

#configurações para o banco de dados
app.config['MYSQL_HOST'] = "localhost" #servidor
app.config['MYSQL_USER'] = "root" #usuário
app.config['MYSQL_PASSWORD'] = '' #senha
app.config['MYSQL_DB'] = 'webstandard' #banco
mysql=MySQL(app)

@app.route("/", methods = ["POST","GET"]) #definindo a rota principal
def index():
    try:
        #atribuindo às variáveis os dados coletados pelo formulário
        nome = request.form['nome'] 
        email = request.form['email']
        data = request.form['data']

        #cadastrando usuário no banco de dados
        cadastra_usuario(nome, email, data)
    except:pass
    return render_template("index.html") #renderiza o arquivo html nesta rota

@app.route("/cadastrar/", methods = ["POST","GET"]) #definindo a rota de cadastro
def cadastrar():
    return render_template("consulta.html")

@app.route("/info/", methods = ["POST","GET"]) #definindo a rota de informações
def info():
    return render_template("info.html")

def cadastra_usuario(nome, email, data):
    # método que cadastra o usuário no banco de dados
    cur = mysql.connection.cursor() # definindo cursor para manipular o banco de dados
    
    #inserindo as informações no banco de dados
    sql = f'INSERT INTO usuarios (nome, email, data) VALUES("{nome}","{email}","{data}")'
    cur.execute(sql)
    
    mysql.connection.commit() #confirma os comandos sql 
    cur.close() #finaliza o cursor

if __name__ == "__main__":
    app.run(host='localhost', port='5000',debug=True)