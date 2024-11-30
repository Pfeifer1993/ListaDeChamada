import unittest
from modelo.aluno_modelo import ModeloAluno
from visao.aluno_visao import VisaoAluno
from controlador.aluno_controlador import ControladorAluno

class MockVisaoAluno:
    def __init__(self, inputs):
        self.inputs = inputs
        self.current = 0

    def solicitar_nome_aluno(self):
        if self.current < len(self.inputs):
            value = self.inputs[self.current]
            self.current += 1
            return value
        return "sair"

    @staticmethod
    def exibir_alunos(alunos):
        return alunos

class TestControladorAluno(unittest.TestCase):
    def test_executar(self):
        modelo = ModeloAluno()
        visao = MockVisaoAluno(["João", "Maria", "sair"])
        controlador = ControladorAluno(modelo, visao)
        controlador.executar()
        self.assertEqual(modelo.obter_alunos(), ["João", "Maria"])

if __name__ == "__main__":
    unittest.main()