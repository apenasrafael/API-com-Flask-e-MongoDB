import pymongo
from datetime import datetime


def inteiro_para_romano(numero):
    if not 0 < numero < 4000:
        return 'O valor deve estar entre 1 e 3999.'

    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    resultado = []

    for i in range(len(ints)):
        contador = int(numero / ints[i])
        resultado.append(nums[i] * contador)
        numero -= ints[i] * contador

    return ''.join(resultado)


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
