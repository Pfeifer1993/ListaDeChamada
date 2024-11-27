class ModeloAluno:
    """
    Classe que gerencia a lista de alunos.
    """
    def __init__(self):
        """
        Inicializa uma lista vazia para os alunos.
        """
        self.alunos = []

    def adicionar_aluno(self, nome):
        """
        Adiciona um aluno à lista.
        :param nome: Nome do aluno a ser adicionado.
        """
        self.alunos.append(nome)

    def obter_alunos(self):
        """
        Retorna a lista de alunos cadastrados.
        :return: Lista de alunos.
        """
        return self.alunos