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

```
ed005_garantia_nathalia/
│
├── sql/
│   ├── schema.sql
│   ├── inserts.sql
│
├── src/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── loja.py
│   │   ├── equipamento.py
│   │   └── garantia.py
│
├── prints/
│   ├── modelo_logico.png
│   ├── consultas_dbeaver.png
│   ├── execucao_terminal.png
│
└── README.md
```

---

## 🧱 3. Modelo Lógico – Entidades e Relacionamentos

**Entidades:**

* **Loja**: representa a empresa que vende os equipamentos.
* **Equipamento**: produto comprado, com data e valor de compra.
* **Garantia**: registro do prazo e descrição da garantia.

**Relacionamentos:**

* Uma **loja** pode vender **vários equipamentos** (1:N).
* Cada **equipamento** possui **uma única garantia** (1:1).

📸 *Print do modelo lógico:*
![modelo\_logico](prints/modelo_logico.png)

---

## 🧮 4. Modelo Físico – Banco de Dados

O banco foi criado no DBeaver com o nome `app_garantia`.
As tabelas foram criadas com **restrições de integridade** (`NOT NULL`, `CHECK`, `UNIQUE`, `ON DELETE`).

📘 Arquivos:

* `schema.sql`: estrutura das tabelas
* `inserts.sql`: dados de exemplo

📸 *Print das consultas no DBeaver:*
![consultas\_dbeaver](prints/consultas_dbeaver.png)

---

## 🔍 5. Consultas SQL Criadas

### 1️⃣ Equipamentos por loja

```sql
SELECT l.nome, e.nome
FROM loja l
JOIN equipamento e ON l.id_loja = e.id_loja;
```

### 2️⃣ Garantias que vencem nos próximos 30 dias

```sql
SELECT e.nome, g.data_fim
FROM garantia g
JOIN equipamento e ON e.id_equipamento = g.id_equipamento
WHERE g.data_fim <= CURRENT_DATE + INTERVAL '30 days';
```

### 3️⃣ Loja com mais garantias vencidas

```sql
SELECT l.nome, COUNT(*) AS qtd_vencidas
FROM garantia g
JOIN equipamento e ON e.id_equipamento = g.id_equipamento
JOIN loja l ON l.id_loja = e.id_loja
WHERE g.data_fim < CURRENT_DATE
GROUP BY l.nome
ORDER BY qtd_vencidas DESC
LIMIT 1;
```

### 4️⃣ Tempo médio de garantia por loja

```sql
SELECT l.nome AS loja,
       ROUND(AVG(EXTRACT(EPOCH FROM (g.data_fim - g.data_inicio)) / 86400)::numeric, 1) AS media_dias
FROM garantia g
JOIN equipamento e ON e.id_equipamento = g.id_equipamento
JOIN loja l ON l.id_loja = e.id_loja
GROUP BY l.nome;
```

---

## 🐍 6. POO – Representação em Python

### Exemplo de classe de modelo

```python
class Equipamento:
    def __init__(self, id, nome, data_compra, preco):
        self.id = id
        self.nome = nome
        self.data_compra = data_compra
        self.preco = preco

    def __str__(self):
        return f"{self.nome} ({self.data_compra})"
```

### Classe de conexão com o banco

```python
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
```

📸 *Print da execução no terminal:*
![execucao\_terminal](prints/execucao_terminal.png)

---

## 💬 7. Reflexão Pessoal

**O que aprendi:**
Aprendi a criar bancos de dados relacionais no PostgreSQL, modelar tabelas com chaves primárias e estrangeiras e conectar o banco ao Python.

**Dificuldades enfrentadas:**
Tive dificuldade na conexão com o banco e no uso do DBeaver no início, mas consegui resolver revisando as configurações e recriando o serviço PostgreSQL corretamente.

**Conexão com o projeto integrador:**
Esse exercício faz parte da base de dados que poderá ser usada futuramente em uma aplicação web completa.

---

## 🧭 8. Boas Práticas e Versionamento

```bash
git commit -m "criação do schema.sql"
git commit -m "implementação da classe Equipamento"
git commit -m "adição de prints e atualização do README"
```

### Arquivos ignorados:

```gitignore
__pycache__/
*.pyc
.env
```

---

## 🏁 9. Conclusão

Este estudo dirigido me ajudou a consolidar o aprendizado em **banco de dados, SQL e POO**, além de reforçar a importância de documentar e versionar corretamente o código no GitHub.
