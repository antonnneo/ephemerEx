import psycopg
import os


class DataBase():
    def __init__(
            self,
            host=os.environ.get("POSTGRES_HOST"),
            port=os.environ.get("POSTGRES_PORT"),
            dbname=os.environ.get("POSTGRES_DBNAME"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD")
        ):
        self.__connection = psycopg.connect(f"""
                                                host={host} 
                                                port={port}
                                                dbname={dbname} 
                                                user={user} 
                                                password={password}
                                            """)
        self.__cursor = self.__connection.cursor()

    def insert(self, text):
        message_id = self.__cursor.execute(f"""INSERT INTO public.messages ("content") VALUES ('{text}') RETURNING id;""").fetchone()[0]
        self.__connection.commit()
        return message_id
    
    def select(self, id):
        return self.__cursor.execute(f"""SELECT content FROM public.messages WHERE id='{id}';""").fetchone()[0]

    def delete(self, id):
        self.__cursor.execute(f"""DELETE FROM messages WHERE id = '{id}';""")
        self.__connection.commit()    
