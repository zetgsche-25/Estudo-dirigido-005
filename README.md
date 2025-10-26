# 🧾 Estudo Dirigido 005 – Banco de Dados e POO
## Sistema de Controle de Garantia de Equipamentos

**Aluna:** Nathalia Zetgsche de Abreu Gomes  
**Banco:** PostgreSQL  
**Linguagem:** Python 3.x  
**IDE:** DBeaver / VS Code  
**Data de entrega:** 24/10  

---

## 🧠 1. Contexto do Projeto
Este projeto faz parte do Estudo Dirigido 005 e tem como objetivo criar um **sistema de controle de garantia de equipamentos**, unindo **Banco de Dados Relacional (PostgreSQL)** e **Programação Orientada a Objetos (Python)**.

A aplicação simula o controle de garantias de produtos vendidos por lojas, registrando informações como data de compra, valor e data de vencimento da garantia.

---

## 🧩 2. Estrutura do Projeto


---

## 🧱 3. Modelo Lógico – Entidades e Relacionamentos

**Entidades:**
- **Loja**: representa a empresa que vende os equipamentos.  
- **Equipamento**: produto comprado, com data e valor de compra.  
- **Garantia**: registro do prazo e descrição da garantia.

**Relacionamentos:**
- Uma **loja** pode vender **vários equipamentos** (1:N).  
- Cada **equipamento** possui **uma única garantia** (1:1).

📸 *Print do modelo lógico:*  
![modelo_logico](prints/modelo_logico.png)

---

## 🧮 4. Modelo Físico – Banco de Dados

O banco foi criado no DBeaver com o nome `app_garantia`.  
As tabelas foram criadas com **restrições de integridade** (`NOT NULL`, `CHECK`, `UNIQUE`, `ON DELETE`).

📘 Arquivos:
- `schema.sql`: estrutura das tabelas  
- `inserts.sql`: dados de exemplo

📸 *Print das consultas no DBeaver:*  
![consultas_dbeaver](prints/consultas_dbeaver.png)

---

## 🔍 5. Consultas SQL Criadas

Exemplos de consultas implementadas:

1. **Equipamentos por loja**
   ```sql
   SELECT l.nome, e.nome
   FROM loja l
   JOIN equipamento e ON l.id_loja = e.id_loja;
SELECT e.nome, g.data_fim
FROM garantia g
JOIN equipamento e ON e.id_equipamento = g.id_equipamento
WHERE g.data_fim <= CURRENT_DATE + INTERVAL '30 days';
SELECT l.nome, COUNT(*) AS qtd_vencidas
FROM garantia g
JOIN equipamento e ON e.id_equipamento = g.id_equipamento
JOIN loja l ON l.id_loja = e.id_loja
WHERE g.data_fim < CURRENT_DATE
GROUP BY l.nome
ORDER BY qtd_vencidas DESC
LIMIT 1;
SELECT l.nome AS loja,
       ROUND(AVG(EXTRACT(EPOCH FROM (g.data_fim - g.data_inicio)) / 86400)::numeric, 1) AS media_dias
FROM garantia g
JOIN equipamento e ON e.id_equipamento = g.id_equipamento
JOIN loja l ON l.id_loja = e.id_loja
GROUP BY l.nome;
class Equipamento:
    def __init__(self, id, nome, data_compra, preco):
        self.id = id
        self.nome = nome
        self.data_compra = data_compra
        self.preco = preco

    def __str__(self):
        return f"{self.nome} ({self.data_compra})"
import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="app_garantia",
            user="postgres",
            password="sua_senha",
            host="localhost",
            port="5432"
        )

    def consultar(self, query):
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            return cur.fetchall()
        except Exception as e:
            print("Erro na consulta:", e)
        finally:
            cur.close()
git commit -m "criação do schema.sql"
git commit -m "implementação da classe Equipamento"
git commit -m "adição de prints e atualização do README"
__pycache__/
*.pyc
.env

---


