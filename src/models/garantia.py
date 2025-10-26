# src/models/garantia.py
class Garantia:
    def __init__(self, id_garantia, id_equipamento, data_inicio, data_fim, descricao=None):
        self.id_garantia = id_garantia
        self.id_equipamento = id_equipamento
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.descricao = descricao

    def __str__(self):
        return f"Garantia {self.id_garantia}: {self.data_inicio} -> {self.data_fim} ({self.descricao})"
