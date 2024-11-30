import unittest
from modelo.aluno_modelo import ModeloAluno

class TestModeloAluno(unittest.TestCase):
    def setUp(self):
        self.modelo = ModeloAluno()

    def test_adicionar_aluno(self):
        self.modelo.adicionar_aluno("João")
        self.assertIn("João", self.modelo.obter_alunos())

    def test_obter_alunos(self):
        self.modelo.adicionar_aluno("Maria")
        self.modelo.adicionar_aluno("Carlos")
        self.assertEqual(self.modelo.obter_alunos(), ["Maria", "Carlos"])

if __name__ == "__main__":
    unittest.main()