# RotaSegura App - API

O RotaSegura App é um aplicativo destinado à criar rotas seguras para que os cidadãos possam ir de um ponto a outro correndo os menores riscos possíveis.

## Descrição

Rota Segura é um aplicativo móvel desenvolvido como parte do Trabalho de Conclusão de Curso (TCC) de Análise e Desenvolvimento de Sistemas no Instituto Federal de Ciência, Educação e Tecnologia (IFSP), campus Guarulhos. O sistema permite que os usuários façam denúncias de incidentes de segurança e, com base nesses dados, traça rotas mais seguras para outros usuários.

## Funcionalidades

- **Denúncia de Incidentes**: Permite aos usuários denunciar incidentes de segurança em determinadas localidades.
- **Traçar Rotas**: Com base nas denúncias, o sistema sugere rotas mais seguras para os usuários.
- **Visualização de Mapa**: Exibe um mapa com os locais das denúncias.
- **Autenticação de Usuário**: Sistema de login e cadastro de usuários.

## Tecnologias Utilizadas

- **Django**: Framework para desenvolvimento da API.

## Configuração

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

- **Nome**: João Luiz de Castro
- **Instituição**: Instituto Federal de Ciência, Educação e Tecnologia (IFSP), campus Guarulhos
- **Ano de Publicação**: 2019
- **Outros Links**:
    - [Github](https://github.com/JooLuiz)
    - [ORCID](https://orcid.org/0009-0003-1669-4633)
    - [Lattes](http://lattes.cnpq.br/0659061239798618)

- **Nome**: Lucas Carvalho Silva
- **Instituição**: Instituto Federal de Ciência, Educação e Tecnologia (IFSP), campus Guarulhos
- **Ano de Publicação**: 2019
- **Outros Links**:
    - [Github](https://github.com/Lucas4500)
    - [Linkedin](https://www.linkedin.com/in/lucas-carvalho-silva-9bb30611a/)

### Participantes

*  Robson Ferreira Lopes(Orientador) - [Linkedin](https://www.linkedin.com/in/flrobson77/)
*  Giovanni Fonseca (co-orientador) - [Linkedin](https://www.linkedin.com/in/giovani-fonseca-ravagnani-disperati-a4494571/)

## Agradecimentos e Inspirações

* Brad from Traversy Media youtube Channel - [bradtraversy](https://github.com/bradtraversy)
* Desejamos mudar o mundo para melhor

## Referências

Para mais detalhes sobre o trabalho acadêmico, acesse o documento completo [aqui](https://pergamum.biblioteca.ifsp.edu.br/acervo/77634).