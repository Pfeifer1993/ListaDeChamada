"""
Módulo para gerenciar a lista de alunos.
Contém a classe ModeloAluno, que oferece métodos para manipular a lista.
"""

from typing import List

class ModeloAluno:
    """
    Gerencia a lista de alunos e fornece métodos para manipulação.
    """
    def __init__(self):
        self.alunos: List[str] = []

    def adicionar_aluno(self, nome: str) -> None:
        """
        Adiciona um aluno à lista.
        """
        self.alunos.append(nome)

    def obter_alunos(self) -> List[str]:
        """
        Retorna a lista de alunos cadastrados.
        """
        return self.alunos

    def limpar_alunos(self) -> None:
        """
        Remove todos os alunos da lista.
        """
        self.alunos.clear()
