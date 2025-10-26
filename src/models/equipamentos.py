# src/models/equipamento.py
class Equipamento:
    def __init__(self, id_equipamento, id_loja, nome, marca, data_compra, preco):
        self.id_equipamento = id_equipamento
        self.id_loja = id_loja
        self.nome = nome
        self.marca = marca
        self.data_compra = data_compra
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - {self.marca} (Comprado em {self.data_compra})"
