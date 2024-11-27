class VisaoAluno:
    """
    Classe responsável pela interação com o usuário.
    """
    @staticmethod
    def exibir_alunos(alunos):
        """
        Exibe a lista de alunos cadastrados.
        :param alunos: Lista de alunos.
        """
        print("Lista de chamada:")
        for indice, aluno in enumerate(alunos, start=1):
            print(f"{indice}. {aluno}")

    @staticmethod
    def solicitar_nome_aluno():
        """
        Solicita o nome do aluno ao usuário.
        :return: Nome do aluno digitado ou 'sair' para finalizar.
        """
        return input("Digite o nome do aluno (ou 'sair' para finalizar): ")