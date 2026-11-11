# Gerenciador de Tarefas

Este projeto servirá para aprimorarmos nossa lógica de programação ao mesmo tempo em que exploramos conceitos e técnicas de programação back-end e fullstack. Vamos utilizar e desenvolver o conceito de MVC (Model-View-Controller) , algumas particularidades da Programação Orientada a Objetos, Programação Funcional, persistência de dados (MySQL), microframework Flask e gerenciador de pacotes do Python (Astral uv).

Alguns passos inciais para preparar o projeto:
1. Caso não esteja instalado, prepare o uv no seu OS. Você encontra o script de instalação no site: <https://docs.astral.sh/uv/getting-started/installation/>
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Faça a incialização do projeto com o comando:
```bash
uv init
```

Até então utilizávamos um Loyout de pacote (Package Layout) denominado flat-layout. O uv adota uma estruturação mais moderna chamada src-layout, que previne erros de implantação comuns chamados `import shadowing` (importações mascaradas).

3. Crie um ambiente virtual do Python:
```bash
uv venv
```
Ative o ambiente virtual se necessário:
```bash
source .venv/Scripts/activate
.venv\Scripts\Activate.ps1 # no PowerShell do Windows
source .venv/bin/activate # no Bash do Linux
```

4. Instale o Flask
```bash
uv add flask
```
Será criado um arquivo uv.lock contendo as dependências (requerimentos) e versões dos pacotes do seu projeto.

5. Crie um arquivo app.py contendo o código inicial do projeto
```python
from flask import Flask

app = Flask(__name__)

@app.route('/test')
def test():
    return 'Servidor online!'
```

6. Teste a aplicação inciando o servidor Flask
```bash
uv run flask run
```