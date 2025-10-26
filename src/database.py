# src/database.py
"""
Database helper para conectar no PostgreSQL e executar queries.
Usa variáveis de ambiente do arquivo .env (via python-dotenv).
"""
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()  # carrega .env da raiz do projeto

DB = {
    "dbname": os.getenv("DB_NAME", "app_garantia"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", ""),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
}

class Database:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(**DB)
        except Exception as e:
            print("Erro ao conectar no banco:", e)
            raise

    def fetchall(self, query, params=None):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(query, params or ())
            return cur.fetchall()
        except Exception as e:
            print("Erro na consulta:", e)
            return []
        finally:
            cur.close()

    def fetchone(self, query, params=None):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(query, params or ())
            return cur.fetchone()
        except Exception as e:
            print("Erro na consulta:", e)
            return None
        finally:
            cur.close()

    def execute(self, query, params=None):
        cur = self.conn.cursor()
        try:
            cur.execute(query, params or ())
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print("Erro ao executar:", e)
            raise
        finally:
            cur.close()

    def close(self):
        if self.conn:
            self.conn.close()
