from datetime import datetime

from tarefas.models.database import Database


class Tarefa:
    """Provê métodos para armazenar, recuperar e processar os dados das
    tarefas criadas a partir do formulário principal.
    """

    def __init__(self, titulo, id=None, data_conclusao=None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao


    def salvarTarefa(self):
        """Salva a tarefa no banco de dados."""

        sql = 'INSERT INTO tarefa (titulo_tarefa, data_conclusao) VALUES (%s, %s);'
        params = (self.titulo, self.data_conclusao)

        with Database() as db:
            db.executar(sql, params)


    @staticmethod
    def listarTarefas() -> list:
        """Retorna uma lista com todas as tarefas cadastradas."""

        sql = '''SELECT id_tarefa, titulo_tarefa, data_conclusao 
        FROM tarefa LIMIT 100; '''

        with Database() as db:
            tarefas_banco = db.executar(sql)

        return tarefas_banco if tarefas_banco else []


    @staticmethod
    def buscarTarefa(id_tarefa):
        """Busca uma tarefa pelo ID e cria um novo objeto Tarefa."""

        sql = """SELECT id_tarefa, titulo_tarefa, data_conclusao
                 FROM tarefa
                 WHERE id_tarefa = %s;"""

        params = (id_tarefa,)

        with Database() as db:
            tarefa_banco = db.executar(sql, params)

        if tarefa_banco:
            tarefa = tarefa_banco[0]

            return Tarefa(
                id=tarefa['id_tarefa'],
                titulo=tarefa['titulo_tarefa'],
                data_conclusao=tarefa['data_conclusao']
            )

        return None


    @staticmethod
    def atualizarTarefa(id_tarefa, titulo, data_conclusao):
        """Atualiza os dados de uma tarefa."""

        sql = """UPDATE tarefa
                 SET titulo_tarefa = %s, data_conclusao = %s
                 WHERE id_tarefa = %s;"""

        params = (titulo, data_conclusao, id_tarefa)

        with Database() as db:
            db.executar(sql, params)


    @staticmethod
    def apagarTarefa(id_tarefa):

        sql = """DELETE FROM tarefa WHERE id_tarefa = %s;"""
        params = (id_tarefa,)

        with Database() as db:
            db.executar(sql, params)


# Área 51 (testes)
# tarefa = Tarefa('Minha nova tarefa')
# tarefa.salvarTarefa()