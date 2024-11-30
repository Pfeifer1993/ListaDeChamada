"""
Script de setup do projeto
"""

from setuptools import setup, find_packages

setup(
    name="ListaDeChamada",
    version="0.1.0",
    description="Projeto para gerenciamento de lista de chamada de alunos.",
    author="Maria Luisa",
    author_email="luisamoraes221@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        # Dependências do projeto
    ],
    extras_require={
        "dev": [
            "pytest",
            "pylint",
            "mypy",
            "flake8",
            "black",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
