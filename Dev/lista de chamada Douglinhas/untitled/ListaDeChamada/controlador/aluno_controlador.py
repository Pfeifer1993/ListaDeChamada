class ControladorAluno:

    def __init__(self, modelo, visao):

        self.modelo = modelo
        self.visao = visao

    def executar(self):

        while True:
            nome = self.visao.solicitar_nome_aluno()
            if not nome.strip():
                self.modelo.exibir_mensagem("O nome não deve ser vazio. Tente novamente.")
                continue
            if not nome.isalpha():
                self.modelo.exibir_mensagem("O nome deve conter apenas letras. Tente novamente.")
                continue
            if nome.lower() == "sair":
                break
            self.modelo.adicionar_aluno(nome)
        self.visao.exibir_alunos(self.modelo.obter_alunos())