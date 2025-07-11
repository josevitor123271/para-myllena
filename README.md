### Passos para Iniciar um projeto Django

Estrutra de pastas
```sh
django-myllena/ # Pasta raiz da aplicação
└── myllena_project/                # Pasta principal do seu projeto Django
    ├── myApp/                     # Seu app Django personalizado (você pode criar vários apps assim)
    │   ├── __pycache__/           # Arquivos compilados do Python (gerados automaticamente, pode ignorar)
    │   ├── migrations/            # Controle de migrações do banco de dados para este app
    │   │   ├── __pycache__/
    │   │   └── __init__.py
    │   ├── templates/             # Pasta para templates HTML deste app
    │   │   └── index.html
    │   ├── __init__.py            # Torna a pasta um pacote Python
    │   ├── admin.py               # Configurações para o admin do Django deste app
    │   ├── apps.py                # Configurações do app
    │   ├── models.py              # Modelos (tabelas do banco de dados) deste app
    │   ├── tests.py               # Testes automatizados deste app
    │   └── views.py               # Funções/classes que respondem às requisições (lógica das páginas)
    ├── myllena_project/           # Pasta do projeto Django (contém configurações globais)
    │   ├── __pycache__/
    │   ├── __init__.py
    │   ├── asgi.py                # Configuração para ASGI (deploy assíncrono)
    │   ├── settings.py            # Configurações globais do projeto (apps instalados, banco, etc)
    │   ├── urls.py                # Rotas globais do projeto (liga URLs a views)
    │   └── wsgi.py                # Configuração para WSGI (deploy tradicional)
    ├── db.sqlite3                 # Banco de dados SQLite padrão do Django
    └── manage.py                  # Script utilitário para comandos Django (migrar, rodar servidor, etc)
```

### Passos

1 - Cria o ambiente virtual (Por causa dos conflitos de versão)

```sh
python -m venv nome_da_sua_venv
```

2 - Ativar ambiente virtual

```sh
# .\venv\Scripts\Activate -> substitua venv pelo nome do seu ambiente virtual
```

3 - Cria um projeto Django (Com ambiente ativado)

```sh
# pip3 install django
```

4 - Cria um projeto django (Na pasta raiz)

```sh
django-myllena/ # Pasta raiz da aplicação
└── myllena_project/                # Pasta principal do seu projeto Django (Cria na pasta raiz /django-myllena)
    ├── myApp/                     # Seu app Django personalizado (você pode criar vários apps assim)
    │   ├── __pycache__/           # Arquivos compilados do Python (gerados automaticamente, pode ignorar)
    │   ├── migrations/            # Controle de migrações do banco de dados para este app
    │   │   ├── __pycache__/
    │   │   └── __init__.py
    │   ├── templates/             # Pasta para templates HTML deste app
    │   │   └── index.html
    │   ├── __init__.py            # Torna a pasta um pacote Python
    │   ├── admin.py               # Configurações para o admin do Django deste app
    │   ├── apps.py                # Configurações do app
    │   ├── models.py              # Modelos (tabelas do banco de dados) deste app
    │   ├── tests.py               # Testes automatizados deste app
    │   └── views.py               # Funções/classes que respondem às requisições (lógica das páginas)
    └── manage.py
```

Comando para criação:

```sh
# django-admin startproject myllena_project
```

5 - Inicializar o projeto (O django procura o arquivo manage.py)

```sh
# cd .\myllena_project\
# python manage.py runserver
```

