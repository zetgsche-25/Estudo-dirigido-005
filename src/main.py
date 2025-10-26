# src/main.py
from database import Database
from models.loja import Loja
from models.equipamento import Equipamento  # CORRETO
from models.garantia import Garantia
from datetime import date

def main():
    db = Database()

    print("== Equipamentos por loja ==")
    q1 = """
    SELECT l.nome AS loja, e.id_equipamento, e.nome AS equipamento, e.marca, e.data_compra
    FROM loja l
    JOIN equipamento e ON e.id_loja = l.id_loja
    ORDER BY l.nome;
    """
    rows = db.fetchall(q1)
    for r in rows:
        print(f"{r['loja']} - [{r['id_equipamento']}] {r['equipamento']} ({r['marca']}) - {r['data_compra']}")

    print("\n== Garantias vencendo nos próximos 30 dias ==")
    q2 = """
    SELECT g.id_garantia, e.nome AS equipamento, l.nome AS loja, g.data_fim
    FROM garantia g
    JOIN equipamento e ON e.id_equipamento = g.id_equipamento
    JOIN loja l ON l.id_loja = e.id_loja
    WHERE g.data_fim BETWEEN CURRENT_DATE AND (CURRENT_DATE + INTERVAL '30 days')
    ORDER BY g.data_fim;
    """
    rows = db.fetchall(q2)
    if rows:
        for r in rows:
            print(f"{r['data_fim']} - {r['loja']} - {r['equipamento']}")
    else:
        print("Nenhuma garantia vence nos próximos 30 dias.")

    print("\n== Loja com maior número de garantias vencidas ==")
    q3 = """
    SELECT l.nome AS loja, COUNT(*) AS garantias_vencidas
    FROM garantia g
    JOIN equipamento e ON e.id_equipamento = g.id_equipamento
    JOIN loja l ON l.id_loja = e.id_loja
    WHERE g.data_fim < CURRENT_DATE
    GROUP BY l.nome
    ORDER BY garantias_vencidas DESC
    LIMIT 1;
    """
    row = db.fetchone(q3)
    if row:
        print(f"{row['loja']} - {row['garantias_vencidas']} garantias vencidas")
    else:
        print("Nenhuma garantia vencida encontrada.")

    print("\n== Tempo médio de garantia por loja (dias) ==")
    q4 = """
    SELECT l.nome AS loja,
           ROUND(AVG(EXTRACT(EPOCH FROM (g.data_fim - g.data_inicio)) / 86400)::numeric, 1) AS media_dias
    FROM garantia g
    JOIN equipamento e ON e.id_equipamento = g.id_equipamento
    JOIN loja l ON l.id_loja = e.id_loja
    GROUP BY l.nome;
    """
    rows = db.fetchall(q4)
    for r in rows:
        print(f"{r['loja']} -> {r['media_dias']} dias")

    db.close()

if __name__ == "__main__":
    main()
