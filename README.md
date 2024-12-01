# ListaDeChamada

**ListaDeChamada** é um projeto de gerenciamento de lista de chamada de alunos, criado com o objetivo de facilitar o controle e a organização das presenças em aulas e eventos.
Projeto cirado utilizando a arquitetura MVC.

## 📄 Descrição

Este sistema permite que o professor ou responsável pela lista de chamada registre os alunos, visualize a presença dos alunos nas aulas e gerencie as informações relacionadas a cada aluno, como seu nome e status de presença.

## 🧩 Funcionalidades

- **Registro de Presença**: Permite marcar presença de alunos para cada aula ou evento.
- **Visualização**: Exibe uma lista dos alunos com seu status de presença.
- **Validação de Dados**: Garante que os nomes dos alunos sejam registrados corretamente, permitindo apenas letras.

## 👀 Overview
![image](https://github.com/user-attachments/assets/2080a3fd-e946-4d78-ad38-bc54c0a8aea4)

## ⚙️ Instalação

Para rodar o projeto em sua máquina local, siga os seguintes passos:

### 1. Clonar o repositório

Clone o repositório do projeto para sua máquina local:

```bash
git clone https://github.com/Pfeifer1993/ListaDeChamada.git
```
### 2. Instalar as dependências

Antes de rodar o projeto, certifique-se de ter o Python instalado na sua máquina. Para instalar as dependências, execute o comando:
```bash
cd lista_de_chamada
```
```bash
pip install -e .
```
```bash
pip install mypy pylint
```
```bash
pip install -r requirements.txt
```
### 3. Rodar o projeto

Depois de instalar as dependências, você pode rodar o projeto executando o arquivo principal main.py:
```bash
python main.py
```

## 🧪 Testes
### Testes unitários
```bash
python -m unittest discover -s tests
```
### Utilização de Lint para análise estática de código
```bash
pylint lista_de_chamada
```
### Uso de mypy para checagem de tipos
```bash
mypy --explicit-package-bases .
```

