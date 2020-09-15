# IService API

API baseada em Geolocalização escrita em Python, Flask, Postgres e Postgis.

Com o Iservice é possível que parceiros cadastrados divulguem seus produtos e serviços em sua região.

# Table of contents
   * [Configurando o ambiente local](#configurando-o-ambiente-local)
   * [Documentation](#documentation)
   * [References](#references)

# Configurando o ambiente local

Uma vez que o docker está instalado em seu computador, execute os seguintes passos:

clonar o projeto

    git clone git@github.com:danilolmoura/iservice-api.git

criar e executar a imagem localmente

    cd iservice-api
    docker-compose build
    docker-compose up -d

Após o passo anterior, a aplicação poderá ser acessada no endereço http://127.0.0.1:5000/

Os logs de execução da aplicação podem ser visualizados através dos comandos abaixo

	docker ps
	docker logs <container_id>

# Documentation

* [Read the docs](https://github.com/danilolmoura/iservice-api/blob/master/docs.md)
 
# References

* [Docker](https://www.docker.com/get-started)
* [Flask](http://flask.palletsprojects.com/en/1.1.x/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [GeoAlchemy2](https://geoalchemy-2.readthedocs.io/en/latest/)
