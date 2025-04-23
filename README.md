# OneSyncApi
## Descrição

Projeto de API da OneSync, projeto que visa integrar e centralizar informações de clientes sobre sistema, como notas de NPS e uso de tracking de ações

## Instalação

1. Baixe o Projeto e configure o arquivo `.env` de acordo com o `.env.example`
2. Inicie o Docker e verifique se tu foi corretamente com os seguintes passos:
```
#Inicia os conteineres e a rede necessários
docker compose up -d

#Verifica se os conteineres estão executando corretamente, util para verificar as portas também
docker compose ps

#Entra na linha de comando do conteiner caso seja necessário
docker compose exec fastapi_app /bin/bash

#Caso seja necessário derrubar o conteiner
docker compose down
```

## Estrutura de arquivos
```
├── app
│   ├── Actions
│   │   ├── Auth.py
│   │   ├── NotaAction.py
│   ├── Schemas
│   │   ├── __init__.py
│   │   └── User.py
│   └── Tables
│   |   ├── __init__.py
│   |   ├── Clientes.py
│   |   ├── Notas.py
│   |   └── Users.py
│   ├── database.py
│   ├── __init__.py
│   ├── main.py
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```
1. A pasta app fica o projeto da FastAPI
  - Actions fica com o controllers, responsavel pelo controle de fluxo de ações na aplicação
  - Schemas fica a estrutura para validar as requests, vou verificar se também consigo estruturar as responses com isso
  - Tables fica com as models para manipular dados e estrutura no banco
    - É importante definir o importe e a table dentro do `__init__.py`, para não precisar importar e usar `User.User`
  - database.py fica com a configuração do banco de dados inicial e a váriaveis que precisa ser importados nos outros arquivos
  - main.py é o arquivo inicial do projeto, que está com as rotas atualmente, mas pretendo mudar depois para ter módulos mais independentes
2. Dockerfile e docker-compose gerenciam o docker e são responsáveis, respectivamente, por criar a imagem com as depêndencias do FastAPI, e subir o contêiner junto com o banco PostgreSQL e a network
3. requirements.txt guarda as depêndecias do projeto python, qualquer novo módulo que precise ser utilizado, é recomendado colocar nesse arquivo com sua versão

