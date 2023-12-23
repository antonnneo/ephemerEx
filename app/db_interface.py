import psycopg

def execute(sql_expression):
    with psycopg.connect("dbname=postgres user=user password=password host=db") as conn:
        with conn.cursor() as cur:
            cur.execute(f"{sql_expression}")
