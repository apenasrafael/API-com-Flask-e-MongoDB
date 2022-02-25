import pandas as pd
from flask import Flask, jsonify, request
from datetime import datetime
from auxiliar import inteiro_para_romano, inserir_no_mongodb


app = Flask(__name__)
data_atual = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")


@app.route('/')
def homepage():
    mensagem = 'Olá, visitante! </br></br>'
    mensagem += 'Essa API retorna informações sobre filmes do <b>TOP 10</b> por ano (até 2020), '
    mensagem += 'de acordo com o <b>IMDB</b>. O site utiliza a nota como critério.</br></br>'
    mensagem += 'Para fazer a busca, indique o ano conforme o padrão abaixo (sem as chaves):</br></br>'
    mensagem += '<li>https://demoapi.apenasrafael.repl.co/top10/<b>{ano}</b></li></br></br>'
    mensagem += 'A API também fornece informações sobre algum número. Siga o seguinte formato '
    mensagem += '(sem as chaves):</br></br>'
    mensagem += '<li>https://demoapi.apenasrafael.repl.co/valor/<b>{numero}</li></b></br></br>'
    mensagem += 'Status da API: <b>ON</b> (' + data_atual + ')'

    return mensagem


@app.route('/valor/<int:numero>')
def valor(numero):
    inserir_no_mongodb(numero, 'Número', browser_info())
    resposta = dict()

    if not 0 < numero < 3999:
        resposta['ERRO'] = inteiro_para_romano(numero)
    else:
        resposta['valor'] = numero
        resposta['romano'] = inteiro_para_romano(numero)
        resposta['ao_quadrado'] = pow(numero, 2)
        resposta['ao_cubo'] = pow(numero, 3)
        resposta['eh_palindromo'] = True if str(numero) == str(numero)[::-1] else False

    return jsonify(resposta)


@app.route('/top10/<int:ano>')
def top10(ano):
    inserir_no_mongodb(ano, 'Ano', browser_info())
    imdb = pd.read_csv('imdb.csv')
    top_dez = imdb.loc[imdb['Released_Year'] == str(ano)][:10]
    filmes = top_dez[['Series_Title', 'IMDB_Rating', 'Runtime', 'Genre', 'Director']]
    contador = 1
    resposta = dict()
    for i in range(len(filmes)):
        aux = dict()
        aux['titulo'] = filmes.iloc[i]['Series_Title']
        aux['nota'] = filmes.iloc[i]['IMDB_Rating']
        aux['duracao'] = filmes.iloc[i]['Runtime']
        aux['genero'] = filmes.iloc[i]['Genre']
        aux['diretor'] = filmes.iloc[i]['Director']
        resposta[contador] = aux
        contador += 1

    return jsonify(resposta)


def browser_info():
    sist_op = request.user_agent.platform
    browser = request.user_agent.browser
    browser_version = request.user_agent.version
    return {'so': sist_op, 'browser': browser, 'browser_version': browser_version}


app.run(host='0.0.0.0')
