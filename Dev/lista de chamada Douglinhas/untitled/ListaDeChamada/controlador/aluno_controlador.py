from modelo.aluno_modelo import ModeloAluno
from visao.aluno_visao import VisaoAluno

"""
Este módulo contém o controlador para gerenciar a lógica entre o modelo e a visão no sistema de alunos.
"""
class ControladorAluno:
    """
    Classe responsável por coordenar as interações entre o modelo e a visão.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, modelo, visao) -> None:
        self.modelo = modelo
        self.visao = visao

    def executar(self) -> None:
        """
        Inicia o loop principal para gerenciar a entrada do usuário e a interação entre modelo e visão.
        """

        while True:
            nome = self.visao.solicitar_nome_aluno()
            if not nome.strip():
                self.visao.exibir_mensagem("O nome não deve ser vazio. Tente novamente.")
                continue
            if not nome.replace(" ", "").isalpha():
                self.visao.exibir_mensagem("O nome deve conter apenas letras. Tente novamente.")
                continue
            if nome.lower() == "sair":
                break
            self.modelo.adicionar_aluno(nome)
        self.visao.exibir_alunos(self.modelo.obter_alunos())
