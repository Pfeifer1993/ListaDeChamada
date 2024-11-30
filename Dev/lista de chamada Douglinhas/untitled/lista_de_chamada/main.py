"""
Main da aplicação ListaDeChamada
"""

import sys
import os
from modelo.aluno_modelo import ModeloAluno
from visao.aluno_visao import VisaoAluno
from controlador.aluno_controlador import ControladorAluno

sys.path.append(os.path.join(os.path.dirname(__file__), 'modelo'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'visao'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'controlador'))

if __name__ == "__main__":
    modelo = ModeloAluno()
    visao = VisaoAluno()
    controlador = ControladorAluno(modelo, visao)
    controlador.executar()
