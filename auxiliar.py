import pymongo
from datetime import datetime


def inserir_no_mongodb(valor, operacao, browser_info):
    cliente = pymongo.MongoClient('<Connection String do MongoDB>')
    database = cliente['<Seu database>']
    collection = database['<A collection específica do database selecionado>']
    
    dicionario = browser_info
    data_atual = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    dicionario['data'] = data_atual
    dicionario['valor'] = valor
    dicionario['operacao'] = operacao
    collection.insert_one(dicionario)
