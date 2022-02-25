# API-com-Flask-e-MongoDB
Olá!

Essa API foi escrita para fins de estudo e utiliza as bibliotecas Flask, pandas e PyMongo.

O arquivo **main.py** contém a implementação principal.  
O arquivo **auxiliar.py** contém funções auxiliares, entre elas a que faz a comunicação com o MongoDB.  
O arquivo **imdb.csv** é a fonte de dados que é lida.  
Por fim, no arquivo **requirements.txt** estão listadas as bibliotecas instaladas (e suas respectivas dependências).  
Para instalação da biblioteca PyMongo, o [site oficial](https://docs.mongodb.com/drivers/pymongo/) do MongoDB recomenda o seguinte comando: **pip install 'pymongo[srv]'**


# Sobre a API

É possível obter informações sobre filmes do TOP 10 por ano (até 2020), de acordo com o IMDB. O site utiliza a nota como critério.



Para fazer a busca, indique o ano conforme o padrão abaixo (sem as chaves):

* https://demoapi.apenasrafael.repl.co/top10/{ano}


A API também fornece informações sobre algum número. Siga o seguinte formato (sem as chaves):

* https://demoapi.apenasrafael.repl.co/valor/{numero}

# Integração com MongoDB
Quando a API é requisitada, é inserido um registro no MongoDB com informações relativas à consulta.
É necessário configurar a conexão com o respectivo caminho do database, assim como o nome do database e a collection escolhida para realizar a inserção.
