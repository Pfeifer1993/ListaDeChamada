class ControladorAluno:
    """
    Classe que controla a lógica do programa, conectando a visão e o modelo.
    """
    def __init__(self, modelo, visao):
        """
        Inicializa o controlador com o modelo e a visão.
        :param modelo: Instância do ModeloAluno.
        :param visao: Instância do VisaoAluno.
        """
        self.modelo = modelo
        self.visao = visao

    def executar(self):
        """
        Executa o fluxo principal do programa.
        """
        while True:
            nome = self.visao.solicitar_nome_aluno()
            if nome.lower() == "sair":
                break
            self.modelo.adicionar_aluno(nome)
        self.visao.exibir_alunos(self.modelo.obter_alunos())