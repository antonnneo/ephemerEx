import psycopg
import random
import string
import os

class Response:
    def __init__(self):
        self.struct = {}

    def instanceId(self):
        self.struct["instanceId"] = os.environ.get("HOSTNAME")

    def status(self, status):
        self.struct["status"] = status

    def error(self, error):
        self.struct["error"] = error

    def message(self, message):
        self.struct["message"] = message



def execute(sql_expression):
    with psycopg.connect(f"""host={os.environ.get('POSTGRES_HOST')} 
                         dbname={os.environ.get('POSTGRES_DBNAME')} 
                         user={os.environ.get('POSTGRES_USER')} 
                         password={os.environ.get('POSTGRES_PASSWORD')}""") as conn:
        with conn.cursor() as cur:
            cur.execute(f"{sql_expression}")
            try:
                return cur.fetchone()[0]
            except:
                pass

def generate_text(length):
    all_characters = string.ascii_letters + string.digits
    random_text = ''.join(random.choice(all_characters) for _ in range(length))
    return random_text
