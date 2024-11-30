"""
Este módulo contém a classe VisaoAluno, que gerencia a interação com o usuário
para exibição e entrada de dados relacionados aos alunos. Ele oferece métodos
para exibir a lista de alunos e solicitar o nome de um aluno, além de exibir
mensagens para o usuário.
"""

from typing import List

class VisaoAluno:
    """Gerencia a interação com o usuário para exibição e entrada de dados."""

    @staticmethod
    def exibir_alunos(alunos: List[str]) -> None:
        """Exibe a lista de alunos cadastrados."""
        print("Lista de chamada:")
        for indice, aluno in enumerate(alunos, start=1):
            print(f"{indice}. {aluno}")

    @staticmethod
    def solicitar_nome_aluno() -> str:
        """Solicita o nome de um aluno ou um comando do usuário."""
        return input("Digite o nome do aluno (ou 'sair' para finalizar): ")

    @staticmethod
    def exibir_mensagem(mensagem: str) -> None:
        """
        Exibe uma mensagem para o usuário.

        Args:
            mensagem (str): Mensagem a ser exibida.
        """
        print(mensagem)
