import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            full_name varchar(255),
            language varchar(5)
            );
"""
        self.execute(sql, commit=True)

    def create_wallet_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Wallets (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            wallet_name varchar(255),
            wallet_number varchar(255),
            currency varchar(255),
            FOREIGN KEY (user_id) REFERENCES Users(id)
            );
            """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())
    

    def add_user(self, id: int, full_name: str, language: str):
        sql = "INSERT OR IGNORE INTO Users(id, full_name, language) VALUES(?, ?, ?)"
        parameters = (id, full_name, language)
        self.execute(sql, parameters, commit=True)
    

    def add_wallet(self, user_id: int, wallet_name: str, wallet_number: str, currency: str):
        sql = "INSERT OR IGNORE INTO Wallets(user_id, wallet_name, wallet_number, currency) VALUES(?, ?, ?, ?)"
        parameters = (user_id, wallet_name, wallet_number, currency)
        self.execute(sql, parameters, commit=True)
    

    def update_full_name(self, id: int, full_name: str):
        sql = "UPDATE Users SET full_name = ? WHERE id = ?"
        parameters = (full_name, id)
        self.execute(sql, parameters, commit=True)
    

    def update_language(self, id: int, language: str):
        sql = "UPDATE Users SET language = ? WHERE id = ?"
        parameters = (language, id)
        self.execute(sql, parameters, commit=True)


    def update_wallet_nuber(self, user_id: int, wallet_name: str, number: str):
        sql = "UPDATE Wallets SET wallet_number = ? WHERE user_id = ? and wallet_name = ?"
        parameters = (number, user_id, wallet_name)
        self.execute(sql, parameters, commit=True)
    
    
