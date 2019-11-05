# Projeto de Arquitetura de Software

## Passos pipenv
- dnf install python-pip
- pip help
- sudo dnf install pipenv

## Na pasta do projeto "app"
- pipenv install 
- pipenv shell
- pipenv run python app.py


### Install Flask
```bash 
pip install Flask
```

## Como implantamos nosso workflow ?

<div style="text-align:justify">

1. A cada nova feature, melhoria ou bugfix o primeiro passo do desenvolvedor é sempre criar uma branch derivada da branch master.

2. O desenvolvedor então implementa os testes unitários necessários, codifica e refatora seu código.

3. Ao concluir tarefas o desenvolvedor realiza seus commits de código.

4. Antes de publicar o novo branch, o desenvolvedor realiza uma nova atualização da sua base de código para evitar ou resolver possíveis conflitos.

5. Após testar, rever seu código e fazer o rebase do código atual. O desenvolvedor publica sua branch remotamente e gera um pull request.
</div>

Fontes: 
* http://aelian.com.br/como-implantamos-nosso-workflow-de-desenvolvimento-de-software/