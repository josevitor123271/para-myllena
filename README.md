### Passos para Iniciar um projeto Django

Estrutra de pastas
```sh
django-myllena/
└── myllena_project/
    ├─ myApp/
    │  ├─ migrations/
    │  │  └─ __init__.py
    │  ├─ __init__.py
    │  ├─ admin.py
    │  ├─ apps.py
    │  ├─ models.py
    │  ├─ tests.py
    │  └─ views.py
    ├─ myllena_project/
    │  ├─ __pycache__/
    │  │  ├─ __init__.cpython-313.pyc
    │  │  ├─ settings.cpython-313.pyc
    │  │  ├─ urls.cpython-313.pyc
    │  │  └─ wsgi.cpython-313.pyc
    │  ├─ __init__.py
    │  ├─ asgi.py
    │  ├─ settings.py
    │  ├─ urls.py
    │  └─ wsgi.py
    ├─ db.sqlite3
    └─ manage.py
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
# pip install django
```

4 - Cria um projeto django (Na pasta raiz)

Comando para criação:

```sh
# django-admin startproject myllena_project
```
Resultado:

```sh
django-myllena/
└── myllena_project/
    ├─ myllena_project/
    │  ├─ __init__.py
    │  ├─ asgi.py
    │  ├─ settings.py
    │  ├─ urls.py
    │  └─ wsgi.py
    └─ manage.py
```

5 - Inicializar o projeto (O django procura o arquivo manage.py dentro myllena_project/)

```sh
# cd .\myllena_project\
# python manage.py runserver
```

E após a inicialização, a estrutura fica assim:

```sh
django-myllena/
└── myllena_project/
    ├─ myllena_project/
    │  ├─ __pycache__/
    │  │  ├─ __init__.cpython-313.pyc
    │  │  ├─ settings.cpython-313.pyc
    │  │  ├─ urls.cpython-313.pyc
    │  │  └─ wsgi.cpython-313.pyc
    │  ├─ __init__.py
    │  ├─ asgi.py
    │  ├─ settings.py
    │  ├─ urls.py
    │  └─ wsgi.py
    ├─ db.sqlite3
    └─ manage.py
```

6 - Criando um app (ainda dentro da pasta do projeto (cd .\myllena_project\))

```sh
# python manage.py startapp myApp
```

E após a criação do app, a estrutura fica assim:

```sh
django-myllena/
└── myllena_project/
    ├─ myApp/
    │  ├─ migrations/
    │  │  └─ __init__.py
    │  ├─ __init__.py
    │  ├─ admin.py
    │  ├─ apps.py
    │  ├─ models.py
    │  ├─ tests.py
    │  └─ views.py
    ├─ myllena_project/
    │  ├─ __pycache__/
    │  │  ├─ __init__.cpython-313.pyc
    │  │  ├─ settings.cpython-313.pyc
    │  │  ├─ urls.cpython-313.pyc
    │  │  └─ wsgi.cpython-313.pyc
    │  ├─ __init__.py
    │  ├─ asgi.py
    │  ├─ settings.py
    │  ├─ urls.py
    │  └─ wsgi.py
    ├─ db.sqlite3
    └─ manage.py
```

7 - Após criar a apliacação, defina-o dentro do objeto installed_app (

```sh
settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myApp',  # Insira seu app aqui
]
```

---

8 - Criando a primeira rota (Sem arquivo html)

Em views.py
```sh
views.py
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Bem vindo ao site da myllena!")  # Criando a primeira rota!
```

9 - Chamando a rota que você criou

Em urls.py
```sh
urls.py
from django.contrib import admin
from django.urls import path

# Importando a views do seu aplicativo (myApp)
from myApp import views

# A views é onde você define as rotas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Chamando a rota home de views
]
```

10 - Inicializando a aplicação

Dentro da pasta myllena_project/
```sh
python manage.py runserver
```

E voalá! Sua primeira página web feita em Django!

A estrutura com a pasta /templates ficará assim:

```sh
myllena_project/
├─ myApp/
│  ├─ __pycache__/
│  │  ├─ __init__.cpython-313.pyc
│  │  ├─ admin.cpython-313.pyc
│  │  ├─ apps.cpython-313.pyc
│  │  ├─ models.cpython-313.pyc
│  │  └─ views.cpython-313.pyc
│  ├─ migrations/
│  │  ├─ __pycache__/
│  │  │  └─ __init__.cpython-313.pyc
│  │  └─ __init__.py
│  ├─ templates/
│  │  └─ index.html
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ models.py
│  ├─ tests.py
│  └─ views.py
├─ myllena_project/
│  ├─ __pycache__/
│  │  ├─ __init__.cpython-313.pyc
│  │  ├─ settings.cpython-313.pyc
│  │  ├─ urls.cpython-313.pyc
│  │  └─ wsgi.cpython-313.pyc
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ db.sqlite3
└─ manage.py

```

---

Agora, criaremos o primeiro arquivo html:

### Passos

1 - Crie a pasta /templates dentro do seu aplicativo (myApp)
E depois, crie index.html

2 - Para estilização, crie outra pasta chamada /static dentro de myApp, depois cria estilos/style.css (ainda dentro de /static)
Obs:

```sh
myllena_project/
├─ myApp/
│  ├─ __pycache__/
│  │  ├─ __init__.cpython-313.pyc
│  │  ├─ admin.cpython-313.pyc
│  │  ├─ apps.cpython-313.pyc
│  │  ├─ models.cpython-313.pyc
│  │  └─ views.cpython-313.pyc
│  ├─ migrations/
│  │  ├─ __pycache__/
│  │  │  └─ __init__.cpython-313.pyc
│  │  └─ __init__.py
│  ├─ static/ # pasta static irá conter nossos estilos css
│  │  └─ estilos/
│  │     └─ style.css
│  ├─ templates/
│  │  └─ index.html
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ models.py
│  ├─ tests.py
│  └─ views.py
├─ myllena_project/
│  ├─ __pycache__/
│  │  ├─ __init__.cpython-313.pyc
│  │  ├─ settings.cpython-313.pyc
│  │  ├─ urls.cpython-313.pyc
│  │  └─ wsgi.cpython-313.pyc
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ db.sqlite3
└─ manage.py

```

Ok, mas como chamar o arquivo html?
Simples, você o chama dentro da rota que você criou anteriormente em views.py

```sh
from django.shortcuts import HttpResponse, render

# Create your views here.
def home(request):
  return render(request, 'index.html')
```

Depois, inicializa a aplicação dentro de myllena_project/

```sh
python manage.py runserver
```

E voalá, mais uma vez! Agora o django renderiza um conteúdo em arquivo html.

---

Por último, adicionaremos estilos CSS para a nossa página. Mas como?

```sh
# Por meio da tag link, chame o arquivo de estilo com seu respectivo caminho relativo na estrutura de pastas.
<link rel="stylesheet" href="{%  static 'estilos/style.css' %}">
```

Ficando assim:

```sh
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  {% load static %}
  <link rel="stylesheet" href="{%  static 'estilos/style.css' %}">
  
  <title> Myllena Site </title>
</head>
<body>

  <h1> Welcome to Myllena Project Home Page </h1>
  
  <!-- Add more content as needed -->
</body>
</html>

# Obs: static é o nome da pasta que você definiu. 

```

---

E mais uma vez, agora seu site em django possui arquivos html e css inclusos.

---
O que tá redondo:
- [x] Estrutura de diretórios tá padrão Django 
- [x] Ambiente virtual ativado direitinho
- [x] Criação de projeto e app separado
- [x] Configuração no INSTALLED_APPS
- [x] Views simples e uso do render()
- [x] Templates funcionando
- [x] Static CSS com {% static %} funcionando
