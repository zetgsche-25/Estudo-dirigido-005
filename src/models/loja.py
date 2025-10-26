# src/models/loja.py
class Loja:
    def __init__(self, id_loja, nome, cnpj, telefone=None, email=None):
        self.id_loja = id_loja
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"{self.nome} (CNPJ: {self.cnpj})"
