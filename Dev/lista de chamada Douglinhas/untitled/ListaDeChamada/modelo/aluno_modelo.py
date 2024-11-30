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
        return self.alunos

    def limpar_alunos(self):
        """
        Remove todos os alunos da lista.
        """
        self.alunos.clear()

    def exibir_mensagem(self, mensagem):
        print(mensagem)