import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash
from config import Config


class Database:
    """Conexão com o banco de dados PostgreSQL e execução de consultas."""

    def __init__(self):
        try:
            self.conn = psycopg2.connect(Config.db_connection_url())
            self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        except psycopg2.OperationalError as e:
            print("Erro ao conectar ao banco de dados:", e)
            self.conn, self.cursor = None, None

    def create_tables(self):
        if not self.conn or not self.cursor:
            print("Conexão inválida. Tabela não criada.")
            return

        query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            user_name VARCHAR(50) NOT NULL,
            user_email VARCHAR(50) UNIQUE NOT NULL,
            user_pass VARCHAR(255) NOT NULL
        );
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            print("Erro ao criar tabela de usuários:", e)

    def add_user(self, user_name, user_email, user_pass):
        if not self.conn or not self.cursor:
            print("Conexão inválida. Usuário não adicionado.")
            return None

        hashed_password = generate_password_hash(user_pass)
        query = """
        INSERT INTO users (user_name, user_email, user_pass) 
        VALUES (%s, %s, %s)
        RETURNING id;
        """
        try:
            self.cursor.execute(query, (user_name, user_email, hashed_password))
            self.conn.commit()
            return self.cursor.fetchone()["id"]
        except psycopg2.IntegrityError:
            self.conn.rollback()
            print(f"Erro: O email '{user_email}' já está registrado.")
            return None
        except psycopg2.Error as e:
            self.conn.rollback()
            print("Erro ao adicionar usuário:", e)
            return None

    def get_user_by_email(self, user_email):
        if not self.conn or not self.cursor:
            print("Conexão inválida. Usuário não encontrado.")
            return None

        query = "SELECT * FROM users WHERE user_email = %s;"
        try:
            self.cursor.execute(query, (user_email,))
            return self.cursor.fetchone()
        except psycopg2.Error as e:
            print("Erro ao buscar usuário pelo email:", e)
            return None
    
    def get_all_users(self):
        if not self.conn or not self.cursor:
            print("Conexão inválida. Não foi possível buscar usuários.")
            return []

        query = "SELECT id, user_name, user_email FROM users;"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            print("Erro ao buscar todos os usuários:", e)
            return []

    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except psycopg2.Error as e:
            print("Erro ao fechar a conexão com o banco de dados:", e)
