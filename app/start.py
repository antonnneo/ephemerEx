from flask import Flask
from db_interface import execute
import random

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    return 'healthy'


@app.route('/new', methods=['POST'])
def new_note():
    execute(f"""
    INSERT INTO messages
    (id, "content", read_counter, read_limit, created)
    VALUES('{random.randint(1, 10000000)}', 'test', true, false, 0);
    """)

    return 'Привет, мир!'


if __name__ == '__main__':
    app.run(debug=False, port=5000, host="0.0.0.0")