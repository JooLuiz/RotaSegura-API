# RotaSegura App - API

O RotaSegura App é um aplicativo destinado à criar rotas seguras para que os cidadãos possam ir de um ponto a outro correndo os menores riscos possíveis.

## Começando

### Pré-requisitos

*  [Python](https://www.python.org/downloads/) - 3.7.3
*  pip - The package manager (installed with python <=3.4)
*  [pipenv](https://docs.pipenv.org/en/latest/) - Python Dev Workflow for Humans
*  [MySql](https://www.mysql.com/downloads/) - OpenSource Database

### Instalação
Utilizando o Console:

1.    Clone o projeto no diretório que desejar.
```
git clone http://git.ifspguarulhos.edu.br/gu1760815/rotasegura-api.git
```

2.  Instale o pipenv.
```
pip install pipenv
```

Utilizando o MYSQL Workbrench ou o PHPMyAdmin:

3.  Crie um database chamado rotasegura.

### Configuração de Ambiente
Utilizando o Console, No diretório do projeto:

1.  Iniciar um Ambiente shell do pipenv.
```
pipenv shell
```

2.  Instale o adaptador de mysql para django.
```
pipenv install ./utils/mysqlclient-1.4.2-cp37-cp37m-win32.whl
```

3.  Acesse a pasta rotasegura dentro da pasta rotasegura.
```
cd rotasegura/rotasegura
```

Utilizando um Console, No diretório do projeto/rotasegura/rotasegura:

4.  Execute as migrations.
```
python manage.py migrate
```

### Iniciando o Servidor
Utilizando o Console, No diretório do projeto/rotasegura/rotasegura:


1.  Inicie o Servidor.
```
python manage.py runserver
```
## Construído com

* [DJango](https://www.djangoproject.com/) - The web framework
* [Knox](https://github.com/James1345/django-rest-knox) - Token Authentication Manager
* [Django Rest Framework](https://www.django-rest-framework.org/) - To create a RESTful API

## Contribuidores

### Autores

* **João Luiz de Castro** - *Sócio* - [JooLuiz](https://github.com/JooLuiz)
* **Lucas Carvalho Silta** - *Sócio* - [LucasCarvalho](https://www.linkedin.com/in/lucas-carvalho-silva-9bb30611a/)

### Participantes

*  Robson Ferreira Lopes(Orientador) - [Linkedin](https://www.linkedin.com/in/flrobson77/)
*  Giovanni Fonseca (co-orientador) - [Linkedin](https://www.linkedin.com/in/giovani-fonseca-ravagnani-disperati-a4494571/)

## Licença

Projeto ainda sem Licença.

## Agradecimentos e Inspirações

* Brad from Traversy Media youtube Channel - [bradtraversy](https://github.com/bradtraversy)
* Desejamos mudar o mundo para melhor
