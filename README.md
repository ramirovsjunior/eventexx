# Eventexx

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/ramirovsjunior/eventexx.svg?branch=master)](https://travis-ci.org/ramirovsjunior/eventexx)


## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.7.1
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

````cosole
git clone git@github.com:ramirovsjunior/eventexx.git /Projetos/wttd
cd /Projetos/wttd
python -m venv .wttd
source .wtdd/bin/activate
pip install -r requirements.txt
cp contrib/venv-sample .env
python manage.py test
````

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma  SECRET_KEY segura para instâcia.
4. Defina DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para o heroku.

````cosole
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# Configuro o email
git push heroku master --force
````