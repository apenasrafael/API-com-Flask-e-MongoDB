import pandas as pd
import roman
from flask import Flask, jsonify, request
from datetime import datetime
from num2words import num2words
from auxiliar import inserir_no_mongodb


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
data_atual = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")


@app.route('/')
def homepage():
    mensagem = 'Olá, <b>visitante!</b> </br></br>'
    mensagem += 'Essa API retorna informações sobre filmes do <b>TOP 10</b> por ano (até 2020), '
    mensagem += 'de acordo com o <b>IMDB</b>. O site utiliza a nota como critério.</br></br>'
    mensagem += 'Para fazer a busca, indique o ano conforme o padrão abaixo (sem as chaves):</br></br>'
    mensagem += '<li>https://api-com-flask-e-mongodb.herokuapp.com/top10/<b>{ano}</b></li></br></br>'
    mensagem += 'A API também fornece informações sobre algum número. Siga o seguinte formato '
    mensagem += '(sem as chaves):</br></br>'
    mensagem += '<li>https://api-com-flask-e-mongodb.herokuapp.com/valor/<b>{numero}</li></b></br></br>'
    mensagem += 'Status da API: <b>ON</b> (' + data_atual + ')'

    return mensagem


@app.route('/valor/<int:numero>')
def valor(numero):
    inserir_no_mongodb(numero, 'Número', browser_info())
    resposta = dict()

    if not 0 <= numero <= 4999:
        resposta['ERRO'] = 'O valor informado deve estar entre 0 e 4999.'
    else:
        resposta['valor'] = numero
        resposta['ao_quadrado'] = pow(numero, 2)
        resposta['ao_cubo'] = pow(numero, 3)
        resposta['eh_palindromo'] = True if str(numero) == str(numero)[::-1] else False
        resposta['num_pt'] = num2words(numero, lang='pt-br')
        resposta['num_pt_ordinal'] = num2words(numero, lang='pt-br', to='ordinal')
        resposta['num_romano'] = roman.toRoman(numero)

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

    if len(resposta) == 0:
        resposta['ERRO'] = 'O ano informado não possui registros.'

    return jsonify(resposta)


def browser_info():
    sist_op = request.user_agent.platform
    browser = request.user_agent.browser
    browser_version = request.user_agent.version
    return {'so': sist_op, 'browser': browser, 'browser_version': browser_version}


if __name__ == '__main__':
    app.run(debug=True)
