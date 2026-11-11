from tkinter import Button

from flask import Flask, redirect, render_template, request, url_for

from tarefas.models.database import init_db
from tarefas.models.tarefa import Tarefa

# Instância única do aplicativo Flask
app = Flask(__name__)

# Inicializa o banco de dados dentro do contexto do app
with app.app_context():
    init_db()

@app.route('/test')
def test():
    return 'Servidor online!'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        titulo_form = request.form.get('tituloTarefa')
        data_conclusao_form = request.form.get('dataConclusao')

        # Se a data estiver vazia, define como None
        data_corrigida = data_conclusao_form if data_conclusao_form != '' else None

        if titulo_form:
            # Instancia e salva a nova tarefa
            tarefa = Tarefa(titulo=titulo_form, data_conclusao=data_corrigida)
            tarefa.salvarTarefa()

        return redirect(url_for('home'))

    # Lista todas as tarefas cadastradas no banco
    tarefas = Tarefa.listarTarefas()

    return render_template(
        'base.html',
        título_da_pagina='Lista de Tarefas do Daniel',
        tarefas_da_pagina=tarefas
    )


# Crie uma nova funcionalidade para apagar cada uma das tarefas cadastradas
@app.route('/delete/<int:id>')
def apagar_id_especificado(id):
    # Código aqui
    
    pass

if __name__ == '__main__':
    app.run(debug=True)