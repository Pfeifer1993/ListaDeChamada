from modelo.aluno_modelo import ModeloAluno
from visao.aluno_visao import VisaoAluno
from controlador.aluno_controlador import ControladorAluno

if __name__ == "__main__":
    modelo = ModeloAluno()
    visao = VisaoAluno()
    controlador = ControladorAluno(modelo, visao)
    controlador.executar()