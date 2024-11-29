import unittest
from visao.aluno_visao import VisaoAluno

class TestVisaoAluno(unittest.TestCase):
    def test_exibir_alunos(self):
        # Simular a exibição de alunos
        alunos = ["João", "Maria"]
        self.assertIsNone(VisaoAluno.exibir_alunos(alunos))

    def test_solicitar_nome_aluno(self):
        # Testar entrada simulada
        pass

if __name__ == "__main__":
    unittest.main()
