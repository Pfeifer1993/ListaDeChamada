class VisaoAluno:
    """Gerencia a interação com o usuário para exibição e entrada de dados."""

    @staticmethod
    def exibir_alunos(alunos):
        """Exibe a lista de alunos cadastrados."""
        print("Lista de chamada:")
        for indice, aluno in enumerate(alunos, start=1):
            print(f"{indice}. {aluno}")

    @staticmethod
    def solicitar_nome_aluno():
        """Solicita o nome de um aluno ou um comando do usuário."""
        return input("Digite o nome do aluno (ou 'sair' para finalizar): ")
