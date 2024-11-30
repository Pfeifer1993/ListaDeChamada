"""
Módulo para gerenciar a lista de alunos.
Contém a classe ModeloAluno, que oferece métodos para manipular a lista.
"""

class ModeloAluno:
    """
    Gerencia a lista de alunos e fornece métodos para manipulação.
    """
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, nome):
        """
        Adiciona um aluno à lista.
        """
        self.alunos.append(nome)

    def obter_alunos(self):
        """
        Retorna a lista de alunos cadastrados.
        """
        return self.alunos

    def limpar_alunos(self):
        """
        Remove todos os alunos da lista.
        """
        self.alunos.clear()
