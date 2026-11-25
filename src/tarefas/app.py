from flask import Flask, redirect, render_template, request, url_for

from tarefas.models.database import init_db
from tarefas.models.tarefa import Tarefa

app = Flask(__name__)


with app.app_context():
    init_db()

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        titulo_form = request.form['tituloTarefa']
        data_conclusao_form = request.form['dataConclusao']

        data_corrigida = data_conclusao_form or None

        tarefa = Tarefa(
            titulo=titulo_form,
            data_conclusao=data_corrigida
        )

        tarefa.salvarTarefa()

        return redirect(url_for('home'))

    tarefas = Tarefa.listarTarefas()

    return render_template(
        'base.html',
        titulo_da_pagina='Minha lista de tarefas',
        tarefas_da_pagina=tarefas,
        tarefa_editando=None
    )


@app.route('/delete/<int:id>')
def apagar_id_especificado(id):

    Tarefa.apagarTarefa(id)

    return redirect(url_for('home'))


"""
TAREFA - UPDATE: Crie uma nova funcionalidade para editar/atualizar cada
uma das tarefas, individualmente. A tarefa deverá ser editada/alterada no
próprio formulário da página `base.html`, Note que você deverá criar:

- Um método no modelo (Tarefa) para carregar uma tarefa salva no banco 
na memória (heap) do computador, instanciando um novo objeto;
- Um método no modelo (Tarefa) para alterar a tarefa co  os novos valores;
- Um link no View/Template (base.html) para chamar a rota do Controller
- O botão `Adicionar` deve se tornar um botão `Atualizar`
- Uma rota no Controller (app.py) para intermediar a operação que aceite
os métodos GET (carregar a tarefa no formulário) e POST (enviar os dados
alterados de volta para o Controller)
- Não use JavaScript.
""" 


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def atualizar_tarefa(id):

    # GET = carregar a tarefa no formulário
    if request.method == 'GET':

        tarefa = Tarefa.buscarTarefa(id)

        return render_template(
            'base.html',
            titulo_da_pagina='Minha lista de tarefas',
            tarefas_da_pagina=Tarefa.listarTarefas(),
            tarefa_editando=tarefa
        )


    # POST = enviar os dados alterados para o banco
    if request.method == 'POST':

        titulo_form = request.form['tituloTarefa']
        data_conclusao_form = request.form['dataConclusao']

        data_corrigida = data_conclusao_form or None

        Tarefa.atualizarTarefa(
            id,
            titulo_form,
            data_corrigida
        )

        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()