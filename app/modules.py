import psycopg
import random
import string


def execute(sql_expression):
    with psycopg.connect("dbname=postgres user=user password=password host=localhost") as conn:
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
