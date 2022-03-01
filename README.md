# API-com-Flask-e-MongoDB
Olá!

Essa API foi escrita para fins de estudo e utiliza as bibliotecas **Flask**, **pandas**, **PyMongo**, **roman** e **num2words**

Link: https://api-com-flask-e-mongodb.herokuapp.com/

O arquivo **main.py** contém a implementação principal.  
O arquivo **auxiliar.py** contém funções auxiliares, entre elas a que faz a comunicação com o MongoDB.  
O arquivo **imdb.csv** é a fonte de dados que é lida.  
Por fim, no arquivo **requirements.txt** estão listadas as bibliotecas instaladas (e suas respectivas dependências).  


# Sobre a API

É possível obter informações (título, diretor, nota, duração e gênero) sobre filmes do TOP 10 por ano (até 2020), de acordo com o IMDB. O site utiliza a nota como critério.



Para fazer a busca, indique o ano conforme o padrão abaixo (sem as chaves):

* https://api-com-flask-e-mongodb.herokuapp.com/top10/{ano}


A API também fornece informações (número escrito por extenso, número romano, número ordinal, etc) sobre algum valor. Siga o seguinte formato (sem as chaves):

* https://api-com-flask-e-mongodb.herokuapp.com/valor/{numero}

# Integração com MongoDB
Quando a API é requisitada, é inserido um registro no MongoDB com informações relativas à consulta.
É necessário configurar a conexão com o respectivo caminho do database, assim como o nome do database e a collection escolhida para realizar a inserção.
